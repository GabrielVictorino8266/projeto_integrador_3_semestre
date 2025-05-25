# add libs
from passlib.context import CryptContext
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from jose import jwt, JWTError
from django.conf import settings
 
import sys
sys.path.append('/app')
from api.settings import mongodb

users_collection = mongodb['users']
refresh_tokens_collection = mongodb['refresh_tokens']  # Nova collection
token_blacklist_collection = mongodb['token_blacklist']  # Nova collection

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """
        Verify a plain password against a hashed password.
    """
    if plain_password == hashed_password:
        return True
    return pwd_context.verify(plain_password, hashed_password)

def get_hash_password(password: str):
    """
        Hash a password using bcrypt.
    """
    return pwd_context.hash(password)

def auth_user(cpf: str, password: str):
    """
        Authenticate a user by checking cpf and password.
    """
    user = users_collection.find_one({"cpf": cpf})

    if not user:
        return None
    
    if not verify_password(password, user.get("password")):
        print("Password verification failed")
        return None
    
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
        Creates a JWT access token
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)

    to_encode.update({"exp": expire})

    enconded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    return enconded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta = None):
    """
        Create a JWT refresh token
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=1)
    
    to_encode.update({"exp": expire, "token_type": "refresh"})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    return encoded_jwt

def decode_token(token:str):
    """
        Decode jwt token
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.SIMPLE_JWT['ALGORITHM']])
        return payload
    except JWTError:
        return None
    
def get_user_from_token(token: str):
    """
        Get user from token
    """
    payload = decode_token(token)
    if not payload: 
        return None
    
    user_id = payload.get("user_id")
    if not user_id:
        return None
    
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        return user
    except:
        return None
    

def store_refresh_token(user_id, refresh_token):
    """
    Armazena refresh token no banco de dados
    """
    try:
        # Invalidar refresh tokens anteriores do usuário (opcional)
        refresh_tokens_collection.update_many(
            {"user_id": ObjectId(user_id)},
            {"$set": {"is_active": False}}
        )
        
        # Armazenar novo refresh token
        refresh_tokens_collection.insert_one({
            "user_id": ObjectId(user_id),
            "token": refresh_token,
            "created_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + timedelta(days=1),
            "is_active": True
        })
        
        print(f"✅ Refresh token armazenado para usuário {user_id}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao armazenar refresh token: {e}")
        return False

def validate_refresh_token(refresh_token):
    """
    Valida se refresh token existe e está ativo no banco
    """
    try:
        # Verificar se token está na blacklist
        if is_token_blacklisted(refresh_token):
            print("❌ Refresh token está na blacklist")
            return None
            
        # Verificar se token existe e está ativo
        token_record = refresh_tokens_collection.find_one({
            "token": refresh_token,
            "is_active": True,
            "expires_at": {"$gt": datetime.utcnow()}
        })
        
        if not token_record:
            print("❌ Refresh token não encontrado ou expirado")
            return None
            
        # Buscar usuário associado
        user = users_collection.find_one({"_id": token_record["user_id"]})
        
        if not user:
            print("❌ Usuário associado ao refresh token não encontrado")
            return None
            
        print("✅ Refresh token válido")
        return user
        
    except Exception as e:
        print(f"❌ Erro ao validar refresh token: {e}")
        return None

def invalidate_refresh_token(refresh_token):
    """
    Invalida um refresh token específico
    """
    try:
        result = refresh_tokens_collection.update_one(
            {"token": refresh_token},
            {"$set": {"is_active": False, "invalidated_at": datetime.utcnow()}}
        )
        
        if result.modified_count > 0:
            print("✅ Refresh token invalidado com sucesso")
            return True
        else:
            print("⚠️ Refresh token não encontrado para invalidar")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao invalidar refresh token: {e}")
        return False

def blacklist_token(token):
    """
    Adiciona token à blacklist (para logout)
    """
    try:
        token_blacklist_collection.insert_one({
            "token": token,
            "blacklisted_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + timedelta(days=1)
        })
        
        print("✅ Token adicionado à blacklist")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao adicionar token à blacklist: {e}")
        return False

def is_token_blacklisted(token):
    """
    Verifica se token está na blacklist
    """
    try:
        result = token_blacklist_collection.find_one({
            "token": token,
            "expires_at": {"$gt": datetime.utcnow()}
        })
        
        return result is not None
        
    except Exception as e:
        print(f"❌ Erro ao verificar blacklist: {e}")
        return False

def cleanup_expired_tokens():
    """
    Remove tokens expirados das collections (executar periodicamente)
    """
    try:
        now = datetime.utcnow()
        
        # Remover refresh tokens expirados
        refresh_result = refresh_tokens_collection.delete_many({
            "expires_at": {"$lt": now}
        })
        
        # Remover tokens da blacklist expirados
        blacklist_result = token_blacklist_collection.delete_many({
            "expires_at": {"$lt": now}
        })
        
        print(f"🧹 Limpeza concluída:")
        print(f"   • Refresh tokens removidos: {refresh_result.deleted_count}")
        print(f"   • Blacklist tokens removidos: {blacklist_result.deleted_count}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na limpeza de tokens: {e}")
        return False
