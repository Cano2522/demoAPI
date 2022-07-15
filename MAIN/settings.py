"""
Django settings for MAIN project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--pchace+rj2%mvla5wh9qwo)@22cuwb$ihrlhrb3!xxolpy=b*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'usuarios',
    'UNIFORMAT',
    'OMNICLAS23',
    'OMNICLAS41',
    'OMNICLAS34',
    'OMNICLAS35',
    'MATERIALES',
    'ROLESORG',
    'DATOSGEOGRAFICOS',
    'PROVEEDORES',
    'UNIDADESMEDIDA',
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    # 'simple_history',
    'drf_yasg',
    "corsheaders",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none'
}

TOKEN_EXPIRED_AFTER_SECONDS = 28800

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'MAIN.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MAIN.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'ccdatabase1',
        'USER': 'Adminccgroup',
        'PASSWORD': '78907ggr9786ccgAEC',
        'HOST': 'consultingconstructionserv.database.windows.net',  
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server', #SQL Server Native Client 11.0
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'usuarios.User'

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000"
# ]

# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000"
# ]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 7000
}

# CORS_ALLOW_ALL_ORIGINS = True # If this is used then CORS_ALLOWED_ORIGINS will not have any effect
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:',
# ] # If this is used, then not need to use CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     'http://localhost:',
# ]

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ORIGIN_ALLOW_ALL_ = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True