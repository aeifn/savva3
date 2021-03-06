"""
Django settings for savva3 project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



TITLE="Лекторий Савватеева"



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/



SITETREE_MODEL_TREE_ITEM = 'savva_menu.MyTreeItem'



MARKDOWN_FILTER_WHITELIST_TAGS = ['a','p','ul','ol','li','br','h1','h2','em']

# Application definition

SITE_ID = 1


GRAPHENE = {
    'SCHEMA': 'savva3.schema.schema'
}

INSTALLED_APPS = [

'django.contrib.sites.apps.SitesConfig',
'django.contrib.humanize.apps.HumanizeConfig',
'django_nyt.apps.DjangoNytConfig',
'mptt',
'sekizai',
'sorl.thumbnail',
'wiki.apps.WikiConfig',
'wiki.plugins.attachments.apps.AttachmentsConfig',
'wiki.plugins.notifications.apps.NotificationsConfig',
'wiki.plugins.images.apps.ImagesConfig',
'wiki.plugins.macros.apps.MacrosConfig',


    'base',
    'jokes',
    'events',
    'savva3',
    'features',
    'finance',
    'rating',
    'sheets',
#    'savva_menu',

#    'sitetree',
    'meta',
    'graphene_django',
    'django_filters',
    'markdown_filter',
    'markdown',
    'embed_video',
    'django_extensions',
    'crispy_forms',
    'bootstrapform',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.sites',
#    'django.contrib.flatpages',
    'django.contrib.sitemaps',
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

ROOT_URLCONF = 'savva3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
    		os.path.join(BASE_DIR, 'templates' ),
	],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "sekizai.context_processors.sekizai",
            ],
        },
    },
]

WSGI_APPLICATION = 'savva3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#LANGUAGE_CODE = 'ru_RU'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static-dist' ),
    )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = '/home/egor/savva3/static/'


