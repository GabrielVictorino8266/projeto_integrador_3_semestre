# add libs
from passlib.context import CryptContext
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from jose import jwt, JWTError
from django.conf import settings

# mongo connection
users_collection = settings.mongodb['users']

pwd_context = CryptContext(schemes=["bcrypt"], depracated="auto")

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

    enconded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
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

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_token(token:str):
    """
        Decode jwt token
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
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
