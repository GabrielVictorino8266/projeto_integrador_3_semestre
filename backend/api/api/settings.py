"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import timedelta
from mongoengine import connect
import os

load_dotenv(override=True)


MONGO_URI = os.environ.get('MONGO_URI')
if not MONGO_URI:
    raise Exception("MONGO_URI não configurada nas variáveis de ambiente")

MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'projeto_teste')
if not MONGO_DB_NAME:
    raise Exception("MONGO_DB_NAME não configurada nas variáveis de ambiente")

# Conexão MongoDB
mongo_client = MongoClient(MONGO_URI)
mongodb = mongo_client[MONGO_DB_NAME]
connect(db=MONGO_DB_NAME, host=MONGO_URI)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MIGRATIONS_DIR = os.environ.get('MIGRATIONS_DIR', str(BASE_DIR / 'database/migrations'))

if not os.path.isdir(MIGRATIONS_DIR):
    raise Exception(f'Diretório de migrações não encontrado: {MIGRATIONS_DIR}')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f5o#ebnrpse8%ylekv7n7&mo*6j*8e3$3u9s(8@1@t*&0kki+('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*'] # Development
# ALLOWED_HOSTS = []

# Swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header usando o esquema Bearer. Exemplo: "Authorization: Bearer <token>"',
        },
    },
    'USE_SESSION_AUTH': False,
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'users',
    'drivers',
    'core'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',  # Algoritmo de assinatura
    'SIGNING_KEY': SECRET_KEY,  # Usa a mesma chave secreta do Django
    'AUTH_HEADER_TYPES': ('Bearer',),  # Prefixo do cabeçalho Authorization
    'USER_ID_FIELD': '_id',  # Campo do ID do usuário no MongoDB
    'USER_ID_CLAIM': 'user_id',  # Nome da claim no token JWT
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5174",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True  # Permite cookies e cabeçalhos de autenticação

# Configurações de sessão
SESSION_COOKIE_HTTPONLY = True  # Previne acesso via JavaScript
SESSION_COOKIE_SECURE = False   # Definir como True em produção (requer HTTPS)
SESSION_COOKIE_SAMESITE = 'Lax'  # Previne CSRF em navegadores modernos

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
