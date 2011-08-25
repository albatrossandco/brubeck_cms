# This is a default Django 1.3 settings file (from django-admin.py 
# startproject) with a couple of additions at the end, mostly.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    # Brubeck only requires one default database, but it must use
    # a geospatially-enabled backend. See 
    # https://docs.djangoproject.com/en/1.3/ref/contrib/gis/
    # db-api/#spatial-backends for details.
    # We have only tested PostGIS setups so far.
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.', # Add 'postgis', 'mysql', 'oracle' or 'spatialite'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# 
# A set of example static media to be served from here is included in 
# this repository at brubeck_cms/media.
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# 
# Most of the project doesn't use this right now, though it'd be a great 
# idea.
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = ''

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = ''

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'brubeck_cms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # 
    # This setting should include this repo's directory at 
    # brubeck_cms/brubeck/templates.
    '',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'template_utils',
    'brubeck.core',
    'brubeck.common',
    'brubeck.management',
    'brubeck.tagging',
    'brubeck.personnel',
    'brubeck.publishing',
    'brubeck.photography',
    'brubeck.multimedia',
    'brubeck.articles',
    'brubeck.blogs',
    'brubeck.design',
    'brubeck.advertising',
    'brubeck.comics',
    'brubeck.games',
    'brubeck.mapping',
    'brubeck.podcasts',
    'brubeck.reporters',
    'brubeck.syndication',
    'brubeck.voxpopuli',
    'brubeck.weather',
    'brubeck.events',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# We're in the process of removing this setting (see issue #28), but for 
# now it's required by our email forms defined in urls.py. Each setting 
# here should contain a valid email address.
EDITORS = {
    'chief': '',
    'photo': '',
    'forum': '',
    'online_dev': '',
}

# Weather reports are based on aviation routine weather reports 
# (METARs). This setting should contain a four-letter ICAO airport code 
# (NOT a three-letter IATA airport code like you might see on your 
# checked luggage). See http://en.wikipedia.org/wiki/ICAO_airport_code 
# for examples.
DEFAULT_METAR_STATION = "KCOU"

# This should allow users to override any of these settings as desired.
try:
    from local_settings import *
except ImportError:
    pass
