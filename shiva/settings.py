# coding=utf-8
"""
Django settings for shiva project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
from django.templatetags.static import static
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=_rz34@7zk#!*lvm%d@wsqzb79l9*ca1+_@s@&ujhem66bz2va'

# SECURITY WARNING: don't run with debug turned on in production!
ON_VIPER = os.getenv('ON_VIPER', "False") == "True"
DEBUG = os.getenv('DJANGO_DEBUG', "False") == "True"
if not ON_VIPER:
    DEBUG = True

ALLOWED_HOSTS = ['shiva.thran.cz']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'constance.backends.database',
    'faces',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shiva.urls'

WSGI_APPLICATION = 'shiva.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(default='mysql://thran:salmun@localhost/shiva')}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'cz-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

if ON_VIPER:
    MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DEFAULT_REWARD = '''
<img src="{}" />
<h3>Štěstí</h3>
'''
DEFAULT_REWARD = DEFAULT_REWARD.format(static("gold_cube.jpg"))

CONSTANCE_CONFIG = {
    'DISTORT': (True, 'Převrácení a jiné úprvy obrázku'),
    'REWARD': (DEFAULT_REWARD, "Odměna"),
    'INFO_TEXT': ("Pro přístup ke zprávě je potřeba určit všechny osoby. <br/> Nápady a postřehy můžete psát k jednotlivým fotkám (jako pokusy). <br/> V případě technických problémů piště na <a href='mailto:thran@centrum.cz'>thran@centrum.cz</a>.", "Info text nad konverzací")
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_SUPERUSER_ONLY = False
