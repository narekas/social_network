# -*- coding: utf-8 -*-

# django-debug-toolbar

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

"""
Django settings for practice_django project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv


# Loading ENV
env_path = Path('.') / '.env'

# env_path = '.test.env'
load_dotenv(dotenv_path=env_path)

# End python-dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-f6@&^a&x2%)680k8q7f^r=@8i+dsguw2gc7r)@6b^0k)2)j%)h'

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/
    'django.contrib.humanize',
    'django_extensions',

    # install pasc
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    'debug_toolbar',
    # 'channels',
    'crispy_forms',
    'ckeditor',
    # Мои приложения
    'blog.apps.BlogConfig',
    # должна быть последней
    # https://pypi.org/project/django-cleanup/
    'django_cleanup.apps.CleanupConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware", # django-debug-toolbar
]

ROOT_URLCONF = 'practice_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# django-allauth
# https://django-allauth.readthedocs.io/en/latest/installation.html

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}


# End django-allauth

WSGI_APPLICATION = 'practice_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/4.1/ref/settings/#static-root

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# https://docs.djangoproject.com/en/4.1/ref/settings/#staticfiles-dirs

STATICFILES_DIRS = [
    # "/home/special.polls.com/polls/static",
    # "/home/polls.com/polls/static",
    # "/opt/webfiles/common",
]

# https://docs.djangoproject.com/en/4.1/ref/settings/#staticfiles-finders

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# https://docs.djangoproject.com/en/4.1/ref/settings/#media-root

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# https://docs.djangoproject.com/en/4.1/ref/settings/#media-url

MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html

CRISPY_TEMPLATE_PACK = 'uni_form'

# End django-crispy-forms


# django-ckeditor

CKEDITOR_CONFIGS = {
'default': {
    'toolbar':'full',
},
}
# CKEDITOR_CONFIGS = {
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
# }

# End django-ckeditor


# django-channels

# ASGI_APPLICATION = "practice_django.routing.application"

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer'
#     },
# }


# End django-channels


# email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smpt.gmail.com'
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')

# End email

GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv('GOOGLE_RECAPTCHA_SECRET_KEY')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# в производстве убрать.
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'