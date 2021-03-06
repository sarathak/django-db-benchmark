"""
Django settings for benchmark project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7=wbvr*l63***3gv5irv(^hx9dut$mmclo&b-v@kjabj6xo%z!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tables',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'benchmark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'benchmark.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DB_ENGINE = os.getenv('DB_ENGINE', 'sqlite')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('DB_FILE', BASE_DIR / 'db.sqlite3'),
    }
}
if DB_ENGINE == 'postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('POSTGRES_DB'),  # Or path to database file if using sqlite3.
            'USER': os.getenv('POSTGRES_USER'),  # Not used with sqlite3.
            'HOST': 'db',  # Not used with sqlite3.
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
        },
    }
elif DB_ENGINE == 'cockroachdb':
    DATABASES = {
        'default': {
            'ENGINE': 'django_cockroachdb',
            'NAME': os.getenv('COCKROACH_DATABASE'),  # Or path to database file if using sqlite3.
            'USER': 'root',  # Not used with sqlite3.
            'HOST': 'db',  # Not used with sqlite3.
            'PASSWORD': '',  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '26257',  # Set to empty string for default. Not used with sqlite3.
        },
    }
elif DB_ENGINE == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_DATABASE'),  # Or path to database file if using sqlite3.
            'USER': os.getenv('MYSQL_USER'),  # Not used with sqlite3.
            'HOST': 'db',  # Not used with sqlite3.
            'PASSWORD': os.getenv('MYSQL_PASSWORD'),  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        },
    }
elif DB_ENGINE == 'mariadb':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_DATABASE'),  # Or path to database file if using sqlite3.
            'USER': os.getenv('MYSQL_USER'),  # Not used with sqlite3.
            'HOST': 'db',  # Not used with sqlite3.
            'PASSWORD': os.getenv('MYSQL_PASSWORD'),  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        },
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROWS_LIST = (1000,)
DB_ENGINES = ['postgresql', 'mysql', 'mariadb', 'sqlite', 'cockroachdb']
