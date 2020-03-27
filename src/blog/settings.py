import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tkxrguur82v*32qzb=q!d&#rx=%7k%tb)al@+vav3u=^0&tu$s'

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
    'posts',
    'ckeditor'
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', #typ jezyka, ktory jest uzywane w templatkach -> umozliwia na przyklad uzycie {{ }}, czy {% %}
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

WSGI_APPLICATION = 'blog.wsgi.application'
#

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True #Internationalizacja - mozna robic w 2 jezykach

USE_L10N = True #obsluguje date/czas itd w zaleznosci od kraju

USE_TZ = True #use timezone - okreslenie czasu i strefy czasowej np. dodania posta (jakiejkolwiek czynnosci)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
#     os.path.join(BASE_DIR)
# ]
#
# # VENV_PATH = os.path.dirname(BASE_DIR)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
print("STATIC_URL: ", STATIC_URL)
MEDIA_URL = '/media/'
print("BASE DIR: ", BASE_DIR)
STATICFILES_DIRS = [ #stąd od będzie brał pliki statyczne (z folderu static_in_env ?)
    os.path.join(BASE_DIR, 'static')
]
print("STATICFILES_DIRS ", STATICFILES_DIRS)
VENV_PATH = os.path.dirname(BASE_DIR)
print("VENV_PATH", VENV_PATH)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root') #So this setting specifies a directory to which Django will copy all the static files from from all files within STATICFILES_DIRS
print("STATIC_ROOT ", STATIC_ROOT)
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')
print("MEDIA_ROOT ", MEDIA_ROOT)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
