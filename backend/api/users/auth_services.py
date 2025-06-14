# users/auth_services.py - Sem Verificação de Usuário Ativo
from passlib.context import CryptContext
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from jose import jwt, JWTError
from django.conf import settings
from mongoengine import connection
import sys

sys.path.append('/app')

def users_collection():
    return connection.get_db()['users']

def refresh_tokens_collection():
    return connection.get_db()['refresh_tokens']

def token_blacklist_collection():
    return connection.get_db()['token_blacklist']

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """
    Verifica se uma senha em texto puro corresponde ao hash armazenado.
    Suporta tanto senhas em texto puro (compatibilidade) quanto hashes bcrypt.
    """
    if plain_password == hashed_password:
        return True
    
    try:
        if hashed_password and hashed_password.startswith('$2'):
            return pwd_context.verify(plain_password, hashed_password)
        return False
    except Exception as e:
        print(f"❌ Erro na verificação de senha: {e}")
        return False

def get_hash_password(password: str):
    """
    Gera um hash bcrypt para uma senha.
    """
    return pwd_context.hash(password)

def auth_user(cpf: str, password: str):
    """
    Autentica um usuário verificando CPF e senha.
    REMOVIDA VERIFICAÇÃO DE USUÁRIO ATIVO.
    """
    print(f"🔍 [AUTH] Tentando autenticar usuário com CPF: {cpf}")
    
    user = users_collection().find_one({"cpf": cpf})

    if not user:
        print(f"❌ [AUTH] Usuário com CPF {cpf} não encontrado")
        return None
    
    stored_password = user.get("password")
    if not verify_password(password, stored_password):
        print("❌ [AUTH] Verificação de senha falhou")
        return None
    
    print(f"✅ [AUTH] Usuário {user.get('nome')} autenticado com sucesso")
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Cria um token JWT de acesso.
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta = None):
    """
    Cria um token JWT de refresh.
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=1)
    
    to_encode.update({"exp": expire, "token_type": "refresh"})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    return encoded_jwt

def decode_token(token: str):
    """
    Decodifica um token JWT.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.SIMPLE_JWT['ALGORITHM']])
        return payload
    except JWTError as e:
        print(f"❌ [TOKEN] Erro JWT ao decodificar: {e}")
        return None
    except Exception as e:
        print(f"❌ [TOKEN] Erro inesperado ao decodificar: {e}")
        return None
    
def get_user_from_token(token: str):
    """
    Obtém um usuário a partir de um token JWT.
    REMOVIDA VERIFICAÇÃO DE USUÁRIO ATIVO.
    """
    print(f"🔍 [TOKEN] Processando token...")
    
    if is_token_blacklisted(token):
        print("❌ [TOKEN] Token está na blacklist")
        return None
    
    payload = decode_token(token)
    if not payload: 
        print("❌ [TOKEN] Payload vazio ou inválido")
        return None
    
    user_id = payload.get("user_id")
    if not user_id:
        print("❌ [TOKEN] user_id não encontrado no payload")
        return None
    
    try:
        user = users_collection().find_one({"_id": ObjectId(user_id)})
        if not user:
            print(f"❌ [TOKEN] Usuário com ID {user_id} não encontrado")
            return None
            
        print(f"✅ [TOKEN] Usuário encontrado: {user.get('name')} - {user.get('cpf')}")
        return user
    except Exception as e:
        print(f"❌ [TOKEN] Erro ao buscar usuário: {e}")
        return None

def store_refresh_token(user_id, refresh_token):
    """
    Armazena refresh token no banco de dados.
    Invalida tokens anteriores do mesmo usuário.
    """
    try:
        refresh_tokens_collection().update_many(
            {"user_id": ObjectId(user_id)},
            {"$set": {"is_active": False, "invalidated_at": datetime.utcnow()}}
        )
        
        # Armazenar novo refresh token
        refresh_tokens_collection().insert_one({
            "user_id": ObjectId(user_id),
            "token": refresh_token,
            "created_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + timedelta(days=1),
            "is_active": True
        })
        
        print(f"✅ [REFRESH] Token armazenado para usuário {user_id}")
        return True
        
    except Exception as e:
        print(f"❌ [REFRESH] Erro ao armazenar token: {e}")
        return False

def validate_refresh_token(refresh_token):
    """
    Valida se refresh token existe e está ativo no banco.
    REMOVIDA VERIFICAÇÃO DE USUÁRIO ATIVO.
    """
    try:
        print(f"🔍 [REFRESH] Validando refresh token...")
        
        if is_token_blacklisted(refresh_token):
            print("❌ [REFRESH] Token está na blacklist")
            return None
            
        token_record = refresh_tokens_collection().find_one({
            "token": refresh_token,
            "is_active": True,
            "expires_at": {"$gt": datetime.utcnow()}
        })
        
        if not token_record:
            print("❌ [REFRESH] Token não encontrado ou expirado")
            return None
            
        user = users_collection().find_one({"_id": token_record["user_id"]})
        
        if not user:
            print("❌ [REFRESH] Usuário associado não encontrado")
            return None
            
        print(f"✅ [REFRESH] Token válido para usuário: {user.get('name')}")
        return user
        
    except Exception as e:
        print(f"❌ [REFRESH] Erro ao validar token: {e}")
        return None

def invalidate_refresh_token(refresh_token):
    """
    Invalida um refresh token específico.
    """
    try:
        result = refresh_tokens_collection().update_one(
            {"token": refresh_token},
            {"$set": {"is_active": False, "invalidated_at": datetime.utcnow()}}
        )
        
        if result.modified_count > 0:
            print("✅ [REFRESH] Token invalidado com sucesso")
            return True
        else:
            print("⚠️ [REFRESH] Token não encontrado para invalidar")
            return False
            
    except Exception as e:
        print(f"❌ [REFRESH] Erro ao invalidar token: {e}")
        return False

def blacklist_token(token):
    """
    Adiciona token à blacklist (usado no logout).
    """
    try:
        token_blacklist_collection().insert_one({
            "token": token,
            "blacklisted_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + timedelta(days=1)
        })
        
        print("✅ [BLACKLIST] Token adicionado à blacklist")
        return True
        
    except Exception as e:
        print(f"❌ [BLACKLIST] Erro ao adicionar token: {e}")
        return False

def is_token_blacklisted(token):
    """
    Verifica se um token está na blacklist.
    """
    try:
        result = token_blacklist_collection().find_one({
            "token": token,
            "expires_at": {"$gt": datetime.utcnow()}
        })
        
        return result is not None
        
    except Exception as e:
        print(f"❌ [BLACKLIST] Erro ao verificar blacklist: {e}")
        return False

def cleanup_expired_tokens():
    """
    Remove tokens expirados das collections.
    Deve ser executado periodicamente via comando Django.
    """
    try:
        now = datetime.utcnow()
        
        # Remover refresh tokens expirados
        refresh_result = refresh_tokens_collection().delete_many({
            "expires_at": {"$lt": now}
        })
        
        # Remover tokens da blacklist expirados
        blacklist_result = token_blacklist_collection().delete_many({
            "expires_at": {"$lt": now}
        })
        
        print(f"🧹 [CLEANUP] Limpeza concluída:")
        print(f"   • Refresh tokens removidos: {refresh_result.deleted_count}")
        print(f"   • Blacklist tokens removidos: {blacklist_result.deleted_count}")
        
        return True
        
    except Exception as e:
        print(f"❌ [CLEANUP] Erro na limpeza: {e}")
        return False

def get_user_refresh_tokens(user_id):
    """
    Obtém todos os refresh tokens ativos de um usuário.
    Útil para mostrar sessões ativas.
    """
    try:
        tokens = list(refresh_tokens_collection().find({
            "user_id": ObjectId(user_id),
            "is_active": True,
            "expires_at": {"$gt": datetime.utcnow()}
        }))
        
        return tokens
        
    except Exception as e:
        print(f"❌ [REFRESH] Erro ao buscar tokens do usuário: {e}")
        return []

def invalidate_all_user_tokens(user_id):
    """
    Invalida todos os tokens de um usuário específico.
    Útil para logout de todas as sessões.
    """
    try:
        # Invalidar todos os refresh tokens do usuário
        refresh_result = refresh_tokens_collection().update_many(
            {"user_id": ObjectId(user_id)},
            {"$set": {"is_active": False, "invalidated_at": datetime.utcnow()}}
        )
        
        print(f"✅ [LOGOUT] {refresh_result.modified_count} tokens invalidados para usuário {user_id}")
        return True
        
    except Exception as e:
        print(f"❌ [LOGOUT] Erro ao invalidar tokens do usuário: {e}")
        return False