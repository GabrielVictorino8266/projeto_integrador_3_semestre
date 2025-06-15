# users/auth_services.py
from passlib.context import CryptContext
from datetime import datetime, timezone
from jose import jwt, JWTError
from django.conf import settings
from mongoengine import connection
import logging
from datetime import timedelta
from bson import ObjectId

logger = logging.getLogger(__name__)

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
    
    db = connection.get_db()
    user = db['users'].find_one({"cpf": cpf})
    if not user:
        logger.error(f"User with CPF {cpf} not found")
        return None
    
    if not verify_password(password, user.get("password")):
        logger.error("Password verification failed")
        return None
    
    logger.info(f"User {user.get('name')} authenticated successfully")
    return {
        "_id": str(user["_id"]),
        "name": user.get("name"),
        "cpf": user.get("cpf"),
        "type": user.get("type")
    }

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
    
    payload = decode_token(token)
    if not payload:
        logger.error("Payload is empty or invalid")
        return None
    
    user_id = payload.get("user_id")
    if not user_id:
        logger.error("No user_id in token payload")
        return None
    
    db = connection.get_db()
    user = db['users'].find_one({"_id": ObjectId(user_id)})
    if not user:
        logger.error(f"User with ID {user_id} not found")
        return None
    
    return {
        "_id": str(user["_id"]),
        "name": user.get("name"),
        "cpf": user.get("cpf"),
        "type": user.get("type")
    }

def store_refresh_token(user_id: str, token: str):
    """Store refresh token"""
    try:
        db = connection.get_db()
        # Store refresh token in a separate collection
        db['refresh_tokens'].update_one(
            {"user_id": user_id},
            {"$set": {
                "token": token,
                "created_at": datetime.now(timezone.utc),
                "expires_at": datetime.now(timezone.utc) + timedelta(days=1)
            }},
            upsert=True
        )
        return True
    except Exception as e:
        logger.error(f"Error storing refresh token: {e}")
        return False

def invalidate_user_tokens(user_id: str):
    """Invalidate all user's tokens"""
    try:
        db = connection.get_db()
        # Remove refresh token
        db['refresh_tokens'].delete_one({"user_id": user_id})
        return True
    except Exception as e:
        logger.error(f"Error invalidating tokens: {e}")
        return False

def is_token_blacklisted(token: str):
    """Check if token is blacklisted"""
    try:
        db = connection.get_db()
        # Check if token is in blacklist
        return db['blacklisted_tokens'].find_one({"token": token}) is not None
    except Exception as e:
        logger.error(f"Error checking blacklist: {e}")
        return False

def blacklist_token(token: str):
    """Add token to blacklist"""
    try:
        db = connection.get_db()
        db['blacklisted_tokens'].insert_one({
            "token": token,
            "blacklisted_at": datetime.now(timezone.utc)
        })
        return True
    except Exception as e:
        logger.error(f"Error blacklisting token: {e}")
        return False

def cleanup_expired_tokens():
    """Cleanup expired tokens"""
    try:
        db = connection.get_db()
        current_time = datetime.now(timezone.utc)
        
        # Cleanup expired refresh tokens
        db['refresh_tokens'].delete_many({"expires_at": {"$lt": current_time}})
        
        # Cleanup expired blacklisted tokens
        db['blacklisted_tokens'].delete_many({"blacklisted_at": {"$lt": current_time - timedelta(days=1)}})
        
        logger.info("Token cleanup completed successfully")
        return True
    except Exception as e:
        logger.error(f"Error cleaning up tokens: {e}")
        return False