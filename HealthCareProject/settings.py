from pathlib import Path
from datetime import timedelta
import os
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-*%7xn10@%!n8o7agwc+m$%vx7-=g^oj!1$3y#0+aa+6rsy=$^p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # unfold theme
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # our apps
    'accounts.apps.AccountsConfig',
    'customer.apps.CustomerConfig',
    'product.apps.ProductConfig',
    'ticket.apps.TicketConfig',
    'about.apps.AboutConfig',
    # third party apps
    'rest_framework',
    'drf_spectacular',
    'django_jalali',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # white noise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HealthCareProject.urls'

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

WSGI_APPLICATION = 'HealthCareProject.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# private network database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'qjAHYTJ1SMD4X8v5jLAEyDoF',
        'HOST': 'hcaredb',
        'PORT': '5432',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',

    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AUTH_USER_MODEL = 'accounts.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5000),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Health Care API',
    'DESCRIPTION': 'an api for landing health care services',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True  # for media settings
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOWED_ORIGINS = [
    "https://hcareapi.liara.run",
    "http://localhost:8000",
    "http://localhost:3000",
]

UNFOLD = {
    "SITE_TITLE": "Health Care API",
    "SITE_HEADER": "Health Care API",
    "SITE_URL": "/",
    "SITE_SYMBOL": "speed",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "ENVIRONMENT": "HealthCareProject.settings.environment_callback",
    "THEME": "dark",

    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
    },
}




def environment_callback(request):
    return ["Development", "warning"]


def badge_callback(request):
    return 3