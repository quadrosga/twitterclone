"""
Django settings for twitterclone project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.management import call_command

# Run migrations automatically (for debugging purposes only)
if os.getenv('RUN_MIGRATIONS', 'False').lower() == 'true':
    call_command('migrate')

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Use SQLite for local development and MySQL for production
if os.getenv('ENVIRONMENT') == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME', 'quadrosga$twitterclone'),
            'USER': os.getenv('DB_USER', 'quadrosga'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'twitterclone'),
            'HOST': os.getenv('DB_HOST', 'quadrosga.mysql.pythonanywhere-services.com'),
            'PORT': os.getenv('DB_PORT', '3306'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': os.environ.get('SQL_DATABASE', BASE_DIR / 'db.sqlite3'),
            'USER': os.environ.get('SQL_USER', 'user'),
            'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
            'HOST': os.environ.get('SQL_HOST', 'localhost'),
            'PORT': os.environ.get('SQL_PORT', '5432'),
        }
    }

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '%yvu#b$-c_duzk!_9x@^6bz5#mo#w3)89m4%-&#^u48i@bxiq$')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'quadrosga.pythonanywhere.com', 'twitterclone-ahpj.onrender.com']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework_simplejwt',
    'tweets',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "twitterclone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "twitterclone.wsgi.application"


# Default SQLite database for local development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Default MySQL database for production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'twitterclone',  # Database name from PythonAnywhere
#         'USER': 'quadrosga',       # Username from PythonAnywhere
#         'PASSWORD': 'twitterclone',   # Password from PythonAnywhere
#         'HOST': 'quadrosga.mysql.pythonanywhere-services.com',  # Host from PythonAnywhere
#         'PORT': '3306',  # Default MySQL port
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'twitterclone',  # Database name from PythonAnywhere
        'USER': 'quadrosga',       # Username from PythonAnywhere
        'PASSWORD': 'twitterclone',   # Password from PythonAnywhere
        'HOST': 'quadrosga.mysql.pythonanywhere-services.com',  # Host from PythonAnywhere
        'PORT': '3306',  # Default MySQL port
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'twitterclone',     
#         'USER': 'twitteruser',     
#         'PASSWORD': 'twitterclone',  
#         'HOST': 'localhost',          
#         'PORT': '5432',               
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'tweets/static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGOUT_URL = '/api/login/'

LOGIN_REDIRECT_URL = "feed"

LOGIN_URL = '/api/login/'

CSRF_TRUSTED_ORIGINS = ['https://twitterclone-ahpj.onrender.com']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}