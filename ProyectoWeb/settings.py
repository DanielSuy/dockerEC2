"""
Django settings for Proyectoweb project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as mensajes_de_error


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(!(ru5d_mzi%it_x5o#m!+o(uenhjob^$z)ui!n87gypj6r%r^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProyectoWebApp',
    'conocenos',
    'blog',
    'contacto',
    'estudiante',
    'asignaciondecursos',
    'registrarse',
    'asignacion',
    'docente',
    'administrativo',
    'crispy_forms',
    'crispy_bootstrap5',
    'media',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
]

ROOT_URLCONF = 'ProyectoWeb.urls'

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
                'asignaciondecursos.context_processor.importe_total_asignaciondecursos',

            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases    database-0980.cbiik664ycf3.us-east-2.rds.amazonaws.com

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "proyecto",
        "USER": "postgres",
        "PASSWORD": "202004811",
        "HOST": "database-0980.cbiik664ycf3.us-east-2.rds.amazonaws.com",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL='/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuracion de email

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS = True
EMAIL_HOST_USER="abch428@gmail.com"
EMAIL_HOST_PASSWORD="wccuzruawobtrnjd"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS={

    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}
"""
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]"""
# stipe

STRIPE_PUBLIC_KEY = 'tu_clave_publica_de_stripe'
STRIPE_SECRET_KEY = 'tu_clave_secreta_de_stripe'

# CustomUser
#AUTH_USER_MODEL = 'administrativo.CustomUser'  
