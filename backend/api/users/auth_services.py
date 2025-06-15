# users/auth_services.py
from passlib.context import CryptContext
from datetime import datetime, timezone
from bson.objectid import ObjectId
from jose import jwt, JWTError
from django.conf import settings
from mongoengine import connection
import logging
from datetime import timedelta

logger = logging.getLogger(__name__)

# Database collections
def users_collection():
    return connection.get_db()['users']

def refresh_tokens_collection():
    return connection.get_db()['refresh_tokens']

def token_blacklist_collection():
    return connection.get_db()['token_blacklist']

# Password handling
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Verify password against hash"""
    if plain_password == hashed_password:
        return True
    try:
        if hashed_password and hashed_password.startswith('$2'):
            return pwd_context.verify(plain_password, hashed_password)
        return False
    except Exception as e:
        logger.error(f"Error verifying password: {e}")
        return False

def get_hash_password(password: str):
    """Generate bcrypt hash for password"""
    return pwd_context.hash(password)

# Authentication
def auth_user(cpf: str, password: str):
    """Authenticate user with CPF and password"""
    logger.info(f"Authenticating user with CPF: {cpf}")
    
    user = users_collection().find_one({"cpf": cpf})
    if not user:
        logger.error(f"User with CPF {cpf} not found")
        return None
    
    if not verify_password(password, user.get("password")):
        logger.error("Password verification failed")
        return None
    
    logger.info(f"User {user.get('name')} authenticated successfully")
    return user

# Token handling
def create_token(data: dict, token_type: str = 'access', expires_hours: int = 1):
    """Create JWT token"""
    expire = datetime.now(timezone.utc) + timedelta(hours=expires_hours)
    to_encode = {
        **data,
        "exp": expire,
        "iat": datetime.now(timezone.utc),
        "token_type": token_type
    }
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SIMPLE_JWT['ALGORITHM'])

def decode_token(token: str):
    """Decode JWT token"""
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.SIMPLE_JWT['ALGORITHM']],
            options={'verify_exp': True}
        )
    except JWTError as e:
        logger.error(f"Error decoding token: {e}")
    except Exception as e:
        logger.error(f"Unexpected error decoding token: {e}")
    return None

# User token management
def get_user_from_token(token: str):
    """Get user from JWT token"""
    logger.info("Processing token...")
    
    if is_token_blacklisted(token):
        logger.error("Token is blacklisted")
        return None
    
    payload = decode_token(token)
    if not payload:
        logger.error("Payload is empty or invalid")
        return None
    
    user_id = payload.get("user_id")
    if not user_id:
        logger.error("user_id not found in payload")
        return None
    
    user = users_collection().find_one({"_id": ObjectId(user_id)})
    if not user:
        logger.error(f"User with ID {user_id} not found")
        return None
    
    logger.info(f"User found: {user.get('name')} - {user.get('cpf')}")
    return user

def store_refresh_token(user_id, token):
    """Store refresh token and invalidate old ones"""
    try:
        # Invalidate old tokens
        refresh_tokens_collection().update_many(
            {"user_id": ObjectId(user_id)},
            {"$set": {"is_active": False}}
        )
        
        # Store new token
        refresh_tokens_collection().insert_one({
            "user_id": ObjectId(user_id),
            "token": token,
            "created_at": datetime.now(timezone.utc),
            "expires_at": datetime.now(timezone.utc) + timedelta(days=1),
            "is_active": True
        })
        
        logger.info(f"Token stored for user {user_id}")
        return True
    except Exception as e:
        logger.error(f"Error storing token: {e}")
        return False

def blacklist_token(token):
    """Add token to blacklist"""
    try:
        token_blacklist_collection().insert_one({
            "token": token,
            "blacklisted_at": datetime.now(timezone.utc),
            "expires_at": datetime.now(timezone.utc) + timedelta(days=1)
        })
        
        logger.info("Token added to blacklist")
        return True
    except Exception as e:
        logger.error(f"Error adding token to blacklist: {e}")
        return False

def invalidate_user_tokens(user_id):
    """Invalidate all user's tokens"""
    try:
        result = refresh_tokens_collection().update_many(
            {"user_id": ObjectId(user_id)},
            {"$set": {"is_active": False}}
        )
        logger.info(f"{result.modified_count} tokens invalidated for user {user_id}")
        return True
    except Exception as e:
        logger.error(f"Error invalidating tokens: {e}")
        return False

def is_token_blacklisted(token):
    """Check if token is blacklisted"""
    try:
        return token_blacklist_collection().find_one({
            "token": token,
            "expires_at": {"$gt": datetime.now(timezone.utc)}
        }) is not None
    except Exception as e:
        logger.error(f"Error checking blacklist: {e}")
        return False

def cleanup_expired_tokens():
    """Cleanup expired tokens"""
    try:
        now = datetime.now(timezone.utc)
        refresh_result = refresh_tokens_collection().delete_many({
            "expires_at": {"$lt": now}
        })
        blacklist_result = token_blacklist_collection().delete_many({
            "expires_at": {"$lt": now}
        })
        
        logger.info(f"Cleanup completed:")
        logger.info(f"   • Refresh tokens removed: {refresh_result.deleted_count}")
        logger.info(f"   • Blacklist tokens removed: {blacklist_result.deleted_count}")
        return True
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")
        return False