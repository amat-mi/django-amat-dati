# -*- coding: utf-8 -*-

import os
import platform
#PAOLO - see: https://docs.djangoproject.com/en/1.4/topics/i18n/translation/#how-django-discovers-language-preference
ugettext = lambda s: s

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = PROJECT_PATH

RUNNING_MACHINE_NAME = platform.node().upper()
IS_DEVELOPMENT_MACHINE = RUNNING_MACHINE_NAME in ['DELLY','DAVIDEPC']

DEBUG = IS_DEVELOPMENT_MACHINE #or RUNNING_MACHINE_NAME in ['WEB371.WEBFACTION.COM']
TEMPLATE_DEBUG = DEBUG

#MNT_PATH = PROJECT_PATH.replace('/var/www/','/mnt/webdata/')
MNT_PATH = PROJECT_PATH

print u'Project: "{}"'.format(PROJECT_PATH)
print u'Running on: "{}"'.format(RUNNING_MACHINE_NAME)
print u'With mnt: "{}"'.format(MNT_PATH)
print u'Development machine: "{}"'.format('yes' if IS_DEVELOPMENT_MACHINE else 'no')
print u'Debug: "{}"'.format('yes' if DEBUG else 'no')

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, \
  FORCE_SCRIPT_NAME

#PAOLO - Ensure those cookies are only sent on secure (ie: https) connections for remote server
#There my be other things to do though, see:
#  http://security.stackexchange.com/questions/8964/trying-to-make-a-django-based-site-use-https-only-not-sure-if-its-secure
if not IS_DEVELOPMENT_MACHINE:
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True

#PAOLO - Send correct HTTP header for images 
#(see: http://stackoverflow.com/questions/16303098/django-development-server-and-mime-types)
#PAOLO - Send correct HTTP header for fonts (though fonts from Google Maps are wrong anyway...) 
#(see: #http://stackoverflow.com/questions/18271257/resource-interpreted-as-font-but-transferred-with-mime-type-font-woff-django)
if DEBUG:
  import mimetypes
  mimetypes.add_type("image/png", ".png", True)
  #mimetypes.add_type("application/font-woff", ".woff", True)
  mimetypes.add_type("application/x-woff", ".woff", True)
   
#PAOLO - following lines are to "mount" project under a subpath of the domain (ie: "example.com/project/")
#WARN!!! The same subpath must be correctly setup in configuring the HTTP front server!!!
if IS_DEVELOPMENT_MACHINE:
  FORCE_SCRIPT_NAME = ''
else:
  FORCE_SCRIPT_NAME = ''

# ATTENZIONE!!! Non funziona se FORCE_SCRIPT_NAME impostato a qualcosa!!!                     
LOGIN_REDIRECT_URL = FORCE_SCRIPT_NAME + '/'          #go to Home Page after Signin

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '01$k%#yn+rb_z_+o&!p3is4y$=r__hpdnk$0xmm1zl3b4lu8s_'

ALLOWED_HOSTS = ['dati.amat-mi.it']

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
     ('Paolo', 'prove_django@oicom.com'),
     ('Davide', 'davide.nuccio@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     #PAOLO - Following is to use the Django REST Framework
    'rest_framework',       
    #PAOLO - Following is for GeoDjango
    'django.contrib.gis',             
   ############
    'tweet',
    'park_server_core',
    'pinf',
    'open',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'server.urls'

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

WSGI_APPLICATION = 'server.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
if IS_DEVELOPMENT_MACHINE:
  DATABASES = {
    'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'ENGINE': 'django.contrib.gis.db.backends.postgis',
# PAOLO - In locale invece uso il nome che sarebbe giusto avere anche in remoto!!!           
          'NAME': 'django_amatdati',                      # Or path to database file if using sqlite3.
          'USER': 'django',                      # Not used with sqlite3.
          'PASSWORD': 'djangopass',                  # Not used with sqlite3.
          'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
  }
else:
  DATABASES = {
      'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'ENGINE': 'django.contrib.gis.db.backends.postgis',
# PAOLO - Per ora uso il nome del vecchio database già esistente, perché non ho la permission per rinominarlo!!!           
#           'NAME': 'django_amatdati',                      # Or path to database file if using sqlite3.
          'NAME': 'django_atmtweet',                      # Or path to database file if using sqlite3.
          'USER': 'django',                      # Not used with sqlite3.
          'PASSWORD': 'djangopass',                  # Not used with sqlite3.
          'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
      }
  }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it-it'

#PAOLO - Make only these languages available
LANGUAGES = (
    ('it', ugettext('Italian')),
)

#PAOLO - Change it from the default (0=Sunday)
FIRST_DAY_OF_WEEK = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

#PAOLO - Use the project locale directory too
LOCALE_PATHS = (
    os.path.abspath(os.path.join(PROJECT_PATH, 'locale')),
)

#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
if IS_DEVELOPMENT_MACHINE:
  MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
else:
  MEDIA_ROOT = os.path.abspath(os.path.join(MNT_PATH, '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
MEDIA_URL = '{}/media/'.format(FORCE_SCRIPT_NAME)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
if IS_DEVELOPMENT_MACHINE:
  STATIC_ROOT = ''
else:
  STATIC_ROOT = os.path.abspath(os.path.join(MNT_PATH, '..', 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
STATIC_URL = '{}/static/'.format(FORCE_SCRIPT_NAME)

STATICFILES_DIRS = (
#     os.path.abspath(os.path.join(BASE_DIR, "../../static/")),
    #PAOLO - Serviamo anche le eventuali UI Client delle varie App, ognuna con un diverso prefisso
    #WARN!!! Sarebbe bello se ogni App "aggiungesse" automaticamente qui la sua directory!!! 
    ('tweet',os.path.abspath(os.path.join(PROJECT_PATH, '..', '..', 'atm-tweet-client/www'))),    
#     ('park',os.path.abspath(os.path.join(PROJECT_PATH, '..', '..', 'park-client/www'))),    
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#PAOLO - Define a suitable value for From field (it will be used for exceptions EMails)
SERVER_EMAIL = 'AMAT Django dati errors <info@amat-mi.it>'

#PAOLO - First line will print EMails to console, second line is for the default "real" SMTP backend
#PAOLO - NOOO!!! Let it always print to console, until we have a SMTP server available!!!
if IS_DEVELOPMENT_MACHINE or True:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
  #PAOLO - This is for sending through local MTA
  #EMAIL_HOST = 'localhost'
  #EMAIL_PORT = 25  
  #PAOLO - This is for sending through some other mailserver
  EMAIL_USE_TLS = True
  EMAIL_HOST = 'xxxxxxxxxx'
  EMAIL_PORT = 25
  EMAIL_HOST_USER = 'xxx@xxx.xxx'
  EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxx'

#WARN!!! La parte sotto è commentata perché la configurazione deve essere esplicita dentro ogni App!!!
#In ogni caso la configurazione di default di DRF è già adeguata, anche per "atm-tweet-server" e la classe:
#  'tweet.pagination.CustomPaginationSerializer'
#non sembra in realtà fare alcunché...
#
# REST_FRAMEWORK = {
#     'PAGINATE_BY': 15,                 # Default to 10
#     'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
#     'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
#     'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'tweet.pagination.CustomPaginationSerializer',
#     'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
# }
