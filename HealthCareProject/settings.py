from pathlib import Path
from datetime import timedelta
import os
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
#TODO
SECRET_KEY = 'django-insecure-*%7xn10@%!n8o7agwc+m$%vx7-=g^oj!1$3y#0+aa+6rsy=$^p'

# SECURITY WARNING: don't run with debug turned on in production!
#TODO
DEBUG = True
#TODO
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



#TODO
# public network database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'root',
#         'PASSWORD': 'lCf0RW9MCLXucCz2KbIdXu7j',
#         'HOST': 'apo.liara.cloud',
#         'PORT': '32122',
#     }
# }

# private db


# docker db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',  # Docker service name
        'PORT': 5432,
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
#TODO 
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
#TODO
CORS_ALLOWED_ORIGINS = True

UNFOLD = {
    "SITE_TITLE": "Health Care API",
    "SITE_HEADER": "Health Care API",
    #TODO url
    "SITE_URL": "https://sunrisesys.ir",
    "SITE_SYMBOL": "clinical_notes",
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
    "THEME": "light",

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
            "50": "240 246 255",
            "100": "224 234 255",
            "200": "198 218 252",
            "300": "144 184 248",
            "400": "103 144 242",
            "500": "79 128 225",
            "600": "70 108 200",
            "700": "59 92 172",
            "800": "50 76 144",
            "900": "40 60 115",
            "950": "20 30 65"
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
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {

                "separator": False,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("داشبرد ادمین"),
                        "icon": "dashboard",  
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
                {
                "separator": False,  
                "collapsible": False, 
                "items": [
                    {
                        "title": _("کاربران"),
                        "icon": "person",  
                        "link": reverse_lazy("admin:accounts_user_changelist"),
                    },

                ],
            },
                {
                "separator": True,  
                "collapsible": True, 
                "title": _("محصول و دسته بندی"),
                "items": [
                    {
                        "title": _("محصولات"),
                        "icon": "display_settings",  
                        "link": reverse_lazy("admin:product_product_changelist"),
                    },
                    {
                        "title": _("دسته بندی محصولات"),
                        "icon": "category",  
                        "link": reverse_lazy("admin:product_category_changelist"),
                    },
                ],
            },

                {
                "separator": True,  
                "collapsible": True, 
                "title": _("تیکت ها"),
                "items": [
                    {
                        "title": _("تماس‌های دریافت‌شده"),
                        "icon": "contacts",  
                        "link": reverse_lazy("admin:ticket_contactus_changelist"),
                    },
                    {
                        "title": _("درخواست دمو"),
                        "icon": "handshake",
                        "link": reverse_lazy("admin:ticket_requestdemo_changelist"),
                    },
                    {
                        "title": _("لینک های ارسال تیکت تماس"),
                        "icon": "webhook",
                        "link": reverse_lazy("admin:ticket_endpointsendcontactus_changelist"),
                    },
                    {
                        "title": _("لینک های ارسال تیکت دمو"),
                        "icon": "webhook",
                        "link": reverse_lazy("admin:ticket_endpointsendrequestdemo_changelist"),
                    },
                    {
                        "title": _("لاگ ارسال تیکت"),
                        "icon": "description",
                        "link": reverse_lazy("admin:ticket_logticket_changelist"),
                    },


                ],
            },

            {
                "separator": True,  
                "collapsible": True, 
                "title": _("بخش مشتریان"),
                "items": [
                    {
                        "title": _("مشتریان"),
                        "icon": "partner_exchange",  
                        "link": reverse_lazy("admin:customer_customer_changelist"),
                    },
                    {
                        "title": _("شهر ها"),
                        "icon": "map",  
                        "link": reverse_lazy("admin:customer_city_changelist"),
                    },
                ],
            },


            {
                "separator": True,  
                "collapsible": True, 
                "title": _("بخش فوتر و هیرو و هدر"),
                "items": [
                    {
                        "title": _("فوتر"),
                        "icon": "stacked_inbox",  
                        "link": reverse_lazy("admin:about_footer_changelist"),
                    },
                    {
                        "title": _("هیرو"),
                        "icon": "inventory_2",
                        "link": reverse_lazy("admin:about_hero_changelist"),
                    },
                                       {
                        "title": _("لینک های هدر"),
                        "icon": "link",
                        "link": reverse_lazy("admin:about_headerlink_changelist"),
                    },
                    {
                        "title": _("متا تگ صفحات"),
                        "icon": "sell",
                        "link": reverse_lazy("admin:about_metatagspage_changelist"),
                    },
                ],
            },


            {
                "separator": True,  
                "collapsible": True, 
                "title": _("دیتا های سایت"),
                "items": [
                    {
                        "title": _("گواهینامه‌ها"),
                        "icon": "developer_guide",
                        "link": reverse_lazy("admin:about_certificate_changelist"),
                    },
                    {
                        "title": _("مدیران"),
                        "icon": "shield_person",
                        "link": reverse_lazy("admin:about_manager_changelist"),
                    },

                ],
            },


        ],
    },





}




def environment_callback(request):
    return ["توسعه", "warning"]


def badge_callback(request):
    return 3