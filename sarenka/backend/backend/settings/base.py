import os
from decouple import config # circleCI


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

USER_CREDENTIALS_DB_NAME = "user_credentials"
USER_CREDENTIALS_DB_FILE = "user_credentials.sqlite3"

CWE_DATABASES_DIR = os.path.join(BASE_DIR, "cwe_databases")
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = "^oa#2a*y#rr-vhoi0m&s4+ph&m5^=iq-7wdiitm1@12p15z151"


# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'api_searcher',
    'api_tools',
    'api_vulnerabilities',
]

GRAPHENE = {
    "SCHEMA": 'backend.settings.schema.schema'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build')
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]


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

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    USER_CREDENTIALS_DB_NAME: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, USER_CREDENTIALS_DB_FILE),
    },
    'cwe_1065': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1065.sqlite3'),
    },
    'cwe_155': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_155.sqlite3'),
    },
    'cwe_609': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_609.sqlite3'),
    },
    'cwe_188': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_188.sqlite3'),
    },
    'cwe_369': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_369.sqlite3'),
    },
    'cwe_1298': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1298.sqlite3'),
    },
    'cwe_74': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_74.sqlite3'),
    },
    'cwe_834': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_834.sqlite3'),
    },
    'cwe_170': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_170.sqlite3'),
    },
    'cwe_1292': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1292.sqlite3'),
    },
    'cwe_923': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_923.sqlite3'),
    },
    'cwe_925': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_925.sqlite3'),
    },
    'cwe_792': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_792.sqlite3'),
    },
    'cwe_185': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_185.sqlite3'),
    },
    'cwe_350': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_350.sqlite3'),
    },
    'cwe_152': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_152.sqlite3'),
    },
    'cwe_409': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_409.sqlite3'),
    },
    'cwe_439': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_439.sqlite3'),
    },
    'cwe_1086': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1086.sqlite3'),
    },
    'cwe_531': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_531.sqlite3'),
    },
    'cwe_646': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_646.sqlite3'),
    },
    'cwe_1046': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1046.sqlite3'),
    },
    'cwe_163': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_163.sqlite3'),
    },
    'cwe_617': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_617.sqlite3'),
    },
    'cwe_412': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_412.sqlite3'),
    },
    'cwe_1273': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1273.sqlite3'),
    },
    'cwe_835': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_835.sqlite3'),
    },
    'cwe_324': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_324.sqlite3'),
    },
    'cwe_914': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_914.sqlite3'),
    },
    'cwe_181': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_181.sqlite3'),
    },
    'cwe_183': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_183.sqlite3'),
    },
    'cwe_270': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_270.sqlite3'),
    },
    'cwe_425': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_425.sqlite3'),
    },
    'cwe_824': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_824.sqlite3'),
    },
    'cwe_1320': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1320.sqlite3'),
    },
    'cwe_942': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_942.sqlite3'),
    },
    'cwe_454': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_454.sqlite3'),
    },
    'cwe_142': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_142.sqlite3'),
    },
    'cwe_200': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_200.sqlite3'),
    },
    'cwe_1243': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1243.sqlite3'),
    },
    'cwe_1329': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1329.sqlite3'),
    },
    'cwe_446': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_446.sqlite3'),
    },
    'cwe_755': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_755.sqlite3'),
    },
    'cwe_1177': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1177.sqlite3'),
    },
    'cwe_363': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_363.sqlite3'),
    },
    'cwe_206': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_206.sqlite3'),
    },
    'cwe_146': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_146.sqlite3'),
    },
    'cwe_78': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_78.sqlite3'),
    },
    'cwe_652': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_652.sqlite3'),
    },
    'cwe_79': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_79.sqlite3'),
    },
    'cwe_460': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_460.sqlite3'),
    },
    'cwe_377': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_377.sqlite3'),
    },
    'cwe_588': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_588.sqlite3'),
    },
    'cwe_619': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_619.sqlite3'),
    },
    'cwe_535': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_535.sqlite3'),
    },
    'cwe_696': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_696.sqlite3'),
    },
    'cwe_530': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_530.sqlite3'),
    },
    'cwe_394': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_394.sqlite3'),
    },
    'cwe_469': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_469.sqlite3'),
    },
    'cwe_775': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_775.sqlite3'),
    },
    'cwe_833': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_833.sqlite3'),
    },
    'cwe_1331': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1331.sqlite3'),
    },
    'cwe_481': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_481.sqlite3'),
    },
    'cwe_672': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_672.sqlite3'),
    },
    'cwe_1062': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1062.sqlite3'),
    },
    'cwe_758': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_758.sqlite3'),
    },
    'cwe_316': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_316.sqlite3'),
    },
    'cwe_1317': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1317.sqlite3'),
    },
    'cwe_553': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_553.sqlite3'),
    },
    'cwe_128': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_128.sqlite3'),
    },
    'cwe_541': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_541.sqlite3'),
    },
    'cwe_1042': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1042.sqlite3'),
    },
    'cwe_493': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_493.sqlite3'),
    },
    'cwe_343': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_343.sqlite3'),
    },
    'cwe_776': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_776.sqlite3'),
    },
    'cwe_1123': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1123.sqlite3'),
    },
    'cwe_154': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_154.sqlite3'),
    },
    'cwe_1055': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1055.sqlite3'),
    },
    'cwe_312': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_312.sqlite3'),
    },
    'cwe_76': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_76.sqlite3'),
    },
    'cwe_579': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_579.sqlite3'),
    },
    'cwe_242': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_242.sqlite3'),
    },
    'cwe_94': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_94.sqlite3'),
    },
    'cwe_1272': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1272.sqlite3'),
    },
    'cwe_841': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_841.sqlite3'),
    },
    'cwe_1190': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1190.sqlite3'),
    },
    'cwe_1326': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1326.sqlite3'),
    },
    'cwe_213': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_213.sqlite3'),
    },
    'cwe_1174': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1174.sqlite3'),
    },
    'cwe_234': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_234.sqlite3'),
    },
    'cwe_605': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_605.sqlite3'),
    },
    'cwe_577': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_577.sqlite3'),
    },
    'cwe_837': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_837.sqlite3'),
    },
    'cwe_663': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_663.sqlite3'),
    },
    'cwe_448': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_448.sqlite3'),
    },
    'cwe_1249': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1249.sqlite3'),
    },
    'cwe_550': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_550.sqlite3'),
    },
    'cwe_690': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_690.sqlite3'),
    },
    'cwe_1281': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1281.sqlite3'),
    },
    'cwe_512': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_512.sqlite3'),
    },
    'cwe_1106': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1106.sqlite3'),
    },
    'cwe_1117': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1117.sqlite3'),
    },
    'cwe_698': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_698.sqlite3'),
    },
    'cwe_1300': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1300.sqlite3'),
    },
    'cwe_262': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_262.sqlite3'),
    },
    'cwe_538': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_538.sqlite3'),
    },
    'cwe_689': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_689.sqlite3'),
    },
    'cwe_1101': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1101.sqlite3'),
    },
    'cwe_358': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_358.sqlite3'),
    },
    'cwe_88': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_88.sqlite3'),
    },
    'cwe_594': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_594.sqlite3'),
    },
    'cwe_1120': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1120.sqlite3'),
    },
    'cwe_1303': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1303.sqlite3'),
    },
    'cwe_839': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_839.sqlite3'),
    },
    'cwe_1084': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1084.sqlite3'),
    },
    'cwe_1121': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1121.sqlite3'),
    },
    'cwe_582': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_582.sqlite3'),
    },
    'cwe_344': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_344.sqlite3'),
    },
    'cwe_648': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_648.sqlite3'),
    },
    'cwe_595': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_595.sqlite3'),
    },
    'cwe_1287': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1287.sqlite3'),
    },
    'cwe_347': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_347.sqlite3'),
    },
    'cwe_103': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_103.sqlite3'),
    },
    'cwe_795': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_795.sqlite3'),
    },
    'cwe_1041': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1041.sqlite3'),
    },
    'cwe_1079': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1079.sqlite3'),
    },
    'cwe_1091': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1091.sqlite3'),
    },
    'cwe_405': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_405.sqlite3'),
    },
    'cwe_1280': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1280.sqlite3'),
    },
    'cwe_336': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_336.sqlite3'),
    },
    'cwe_357': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_357.sqlite3'),
    },
    'cwe_160': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_160.sqlite3'),
    },
    'cwe_178': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_178.sqlite3'),
    },
    'cwe_838': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_838.sqlite3'),
    },
    'cwe_267': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_267.sqlite3'),
    },
    'cwe_73': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_73.sqlite3'),
    },
    'cwe_228': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_228.sqlite3'),
    },
    'cwe_682': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_682.sqlite3'),
    },
    'cwe_639': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_639.sqlite3'),
    },
    'cwe_204': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_204.sqlite3'),
    },
    'cwe_1271': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1271.sqlite3'),
    },
    'cwe_174': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_174.sqlite3'),
    },
    'cwe_331': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_331.sqlite3'),
    },
    'cwe_1075': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1075.sqlite3'),
    },
    'cwe_102': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_102.sqlite3'),
    },
    'cwe_1077': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1077.sqlite3'),
    },
    'cwe_495': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_495.sqlite3'),
    },
    'cwe_248': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_248.sqlite3'),
    },
    'cwe_484': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_484.sqlite3'),
    },
    'cwe_273': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_273.sqlite3'),
    },
    'cwe_140': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_140.sqlite3'),
    },
    'cwe_364': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_364.sqlite3'),
    },
    'cwe_1262': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1262.sqlite3'),
    },
    'cwe_447': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_447.sqlite3'),
    },
    'cwe_261': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_261.sqlite3'),
    },
    'cwe_195': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_195.sqlite3'),
    },
    'cwe_313': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_313.sqlite3'),
    },
    'cwe_554': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_554.sqlite3'),
    },
    'cwe_283': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_283.sqlite3'),
    },
    'cwe_482': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_482.sqlite3'),
    },
    'cwe_338': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_338.sqlite3'),
    },
    'cwe_457': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_457.sqlite3'),
    },
    'cwe_89': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_89.sqlite3'),
    },
    'cwe_116': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_116.sqlite3'),
    },
    'cwe_549': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_549.sqlite3'),
    },
    'cwe_590': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_590.sqlite3'),
    },
    'cwe_1267': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1267.sqlite3'),
    },
    'cwe_395': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_395.sqlite3'),
    },
    'cwe_520': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_520.sqlite3'),
    },
    'cwe_223': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_223.sqlite3'),
    },
    'cwe_1246': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1246.sqlite3'),
    },
    'cwe_599': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_599.sqlite3'),
    },
    'cwe_628': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_628.sqlite3'),
    },
    'cwe_345': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_345.sqlite3'),
    },
    'cwe_413': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_413.sqlite3'),
    },
    'cwe_548': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_548.sqlite3'),
    },
    'cwe_403': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_403.sqlite3'),
    },
    'cwe_340': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_340.sqlite3'),
    },
    'cwe_421': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_421.sqlite3'),
    },
    'cwe_680': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_680.sqlite3'),
    },
    'cwe_305': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_305.sqlite3'),
    },
    'cwe_362': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_362.sqlite3'),
    },
    'cwe_782': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_782.sqlite3'),
    },
    'cwe_1255': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1255.sqlite3'),
    },
    'cwe_514': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_514.sqlite3'),
    },
    'cwe_1313': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1313.sqlite3'),
    },
    'cwe_692': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_692.sqlite3'),
    },
    'cwe_536': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_536.sqlite3'),
    },
    'cwe_332': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_332.sqlite3'),
    },
    'cwe_591': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_591.sqlite3'),
    },
    'cwe_1258': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1258.sqlite3'),
    },
    'cwe_1264': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1264.sqlite3'),
    },
    'cwe_916': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_916.sqlite3'),
    },
    'cwe_1099': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1099.sqlite3'),
    },
    'cwe_603': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_603.sqlite3'),
    },
    'cwe_153': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_153.sqlite3'),
    },
    'cwe_669': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_669.sqlite3'),
    },
    'cwe_208': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_208.sqlite3'),
    },
    'cwe_406': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_406.sqlite3'),
    },
    'cwe_1004': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1004.sqlite3'),
    },
    'cwe_1024': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1024.sqlite3'),
    },
    'cwe_1039': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1039.sqlite3'),
    },
    'cwe_302': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_302.sqlite3'),
    },
    'cwe_790': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_790.sqlite3'),
    },
    'cwe_657': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_657.sqlite3'),
    },
    'cwe_915': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_915.sqlite3'),
    },
    'cwe_300': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_300.sqlite3'),
    },
    'cwe_289': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_289.sqlite3'),
    },
    'cwe_263': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_263.sqlite3'),
    },
    'cwe_687': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_687.sqlite3'),
    },
    'cwe_1107': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1107.sqlite3'),
    },
    'cwe_1240': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1240.sqlite3'),
    },
    'cwe_131': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_131.sqlite3'),
    },
    'cwe_325': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_325.sqlite3'),
    },
    'cwe_1056': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1056.sqlite3'),
    },
    'cwe_348': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_348.sqlite3'),
    },
    'cwe_1332': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1332.sqlite3'),
    },
    'cwe_222': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_222.sqlite3'),
    },
    'cwe_827': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_827.sqlite3'),
    },
    'cwe_453': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_453.sqlite3'),
    },
    'cwe_1068': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1068.sqlite3'),
    },
    'cwe_1289': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1289.sqlite3'),
    },
    'cwe_1060': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1060.sqlite3'),
    },
    'cwe_1097': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1097.sqlite3'),
    },
    'cwe_321': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_321.sqlite3'),
    },
    'cwe_662': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_662.sqlite3'),
    },
    'cwe_627': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_627.sqlite3'),
    },
    'cwe_1327': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1327.sqlite3'),
    },
    'cwe_1066': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1066.sqlite3'),
    },
    'cwe_307': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_307.sqlite3'),
    },
    'cwe_515': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_515.sqlite3'),
    },
    'cwe_912': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_912.sqlite3'),
    },
    'cwe_80': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_80.sqlite3'),
    },
    'cwe_108': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_108.sqlite3'),
    },
    'cwe_1312': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1312.sqlite3'),
    },
    'cwe_258': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_258.sqlite3'),
    },
    'cwe_921': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_921.sqlite3'),
    },
    'cwe_184': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_184.sqlite3'),
    },
    'cwe_257': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_257.sqlite3'),
    },
    'cwe_623': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_623.sqlite3'),
    },
    'cwe_788': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_788.sqlite3'),
    },
    'cwe_762': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_762.sqlite3'),
    },
    'cwe_1072': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1072.sqlite3'),
    },
    'cwe_1087': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1087.sqlite3'),
    },
    'cwe_296': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_296.sqlite3'),
    },
    'cwe_654': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_654.sqlite3'),
    },
    'cwe_368': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_368.sqlite3'),
    },
    'cwe_1104': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1104.sqlite3'),
    },
    'cwe_556': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_556.sqlite3'),
    },
    'cwe_510': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_510.sqlite3'),
    },
    'cwe_653': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_653.sqlite3'),
    },
    'cwe_917': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_917.sqlite3'),
    },
    'cwe_1322': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1322.sqlite3'),
    },
    'cwe_1263': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1263.sqlite3'),
    },
    'cwe_1244': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1244.sqlite3'),
    },
    'cwe_765': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_765.sqlite3'),
    },
    'cwe_327': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_327.sqlite3'),
    },
    'cwe_144': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_144.sqlite3'),
    },
    'cwe_1098': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1098.sqlite3'),
    },
    'cwe_1285': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1285.sqlite3'),
    },
    'cwe_502': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_502.sqlite3'),
    },
    'cwe_114': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_114.sqlite3'),
    },
    'cwe_807': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_807.sqlite3'),
    },
    'cwe_555': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_555.sqlite3'),
    },
    'cwe_1105': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1105.sqlite3'),
    },
    'cwe_1232': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1232.sqlite3'),
    },
    'cwe_237': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_237.sqlite3'),
    },
    'cwe_644': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_644.sqlite3'),
    },
    'cwe_304': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_304.sqlite3'),
    },
    'cwe_244': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_244.sqlite3'),
    },
    'cwe_1247': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1247.sqlite3'),
    },
    'cwe_416': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_416.sqlite3'),
    },
    'cwe_686': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_686.sqlite3'),
    },
    'cwe_165': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_165.sqlite3'),
    },
    'cwe_1021': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1021.sqlite3'),
    },
    'cwe_424': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_424.sqlite3'),
    },
    'cwe_1049': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1049.sqlite3'),
    },
    'cwe_1266': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1266.sqlite3'),
    },
    'cwe_317': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_317.sqlite3'),
    },
    'cwe_1277': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1277.sqlite3'),
    },
    'cwe_1248': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1248.sqlite3'),
    },
    'cwe_606': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_606.sqlite3'),
    },
    'cwe_297': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_297.sqlite3'),
    },
    'cwe_1316': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1316.sqlite3'),
    },
    'cwe_271': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_271.sqlite3'),
    },
    'cwe_476': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_476.sqlite3'),
    },
    'cwe_578': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_578.sqlite3'),
    },
    'cwe_98': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_98.sqlite3'),
    },
    'cwe_655': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_655.sqlite3'),
    },
    'cwe_1118': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1118.sqlite3'),
    },
    'cwe_826': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_826.sqlite3'),
    },
    'cwe_544': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_544.sqlite3'),
    },
    'cwe_85': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_85.sqlite3'),
    },
    'cwe_1092': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1092.sqlite3'),
    },
    'cwe_219': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_219.sqlite3'),
    },
    'cwe_1302': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1302.sqlite3'),
    },
    'cwe_828': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_828.sqlite3'),
    },
    'cwe_280': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_280.sqlite3'),
    },
    'cwe_1122': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1122.sqlite3'),
    },
    'cwe_683': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_683.sqlite3'),
    },
    'cwe_224': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_224.sqlite3'),
    },
    'cwe_732': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_732.sqlite3'),
    },
    'cwe_323': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_323.sqlite3'),
    },
    'cwe_911': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_911.sqlite3'),
    },
    'cwe_764': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_764.sqlite3'),
    },
    'cwe_1230': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1230.sqlite3'),
    },
    'cwe_1282': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1282.sqlite3'),
    },
    'cwe_1124': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1124.sqlite3'),
    },
    'cwe_684': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_684.sqlite3'),
    },
    'cwe_393': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_393.sqlite3'),
    },
    'cwe_821': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_821.sqlite3'),
    },
    'cwe_1054': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1054.sqlite3'),
    },
    'cwe_125': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_125.sqlite3'),
    },
    'cwe_584': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_584.sqlite3'),
    },
    'cwe_1291': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1291.sqlite3'),
    },
    'cwe_1222': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1222.sqlite3'),
    },
    'cwe_589': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_589.sqlite3'),
    },
    'cwe_472': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_472.sqlite3'),
    },
    'cwe_650': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_650.sqlite3'),
    },
    'cwe_378': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_378.sqlite3'),
    },
    'cwe_1083': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1083.sqlite3'),
    },
    'cwe_124': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_124.sqlite3'),
    },
    'cwe_1253': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1253.sqlite3'),
    },
    'cwe_260': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_260.sqlite3'),
    },
    'cwe_456': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_456.sqlite3'),
    },
    'cwe_230': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_230.sqlite3'),
    },
    'cwe_601': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_601.sqlite3'),
    },
    'cwe_449': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_449.sqlite3'),
    },
    'cwe_1276': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1276.sqlite3'),
    },
    'cwe_475': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_475.sqlite3'),
    },
    'cwe_1279': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1279.sqlite3'),
    },
    'cwe_286': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_286.sqlite3'),
    },
    'cwe_1229': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1229.sqlite3'),
    },
    'cwe_282': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_282.sqlite3'),
    },
    'cwe_284': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_284.sqlite3'),
    },
    'cwe_72': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_72.sqlite3'),
    },
    'cwe_354': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_354.sqlite3'),
    },
    'cwe_705': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_705.sqlite3'),
    },
    'cwe_1067': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1067.sqlite3'),
    },
    'cwe_1220': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1220.sqlite3'),
    },
    'cwe_749': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_749.sqlite3'),
    },
    'cwe_451': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_451.sqlite3'),
    },
    'cwe_759': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_759.sqlite3'),
    },
    'cwe_710': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_710.sqlite3'),
    },
    'cwe_568': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_568.sqlite3'),
    },
    'cwe_583': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_583.sqlite3'),
    },
    'cwe_1260': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1260.sqlite3'),
    },
    'cwe_1250': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1250.sqlite3'),
    },
    'cwe_1288': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1288.sqlite3'),
    },
    'cwe_1325': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1325.sqlite3'),
    },
    'cwe_1236': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1236.sqlite3'),
    },
    'cwe_1164': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1164.sqlite3'),
    },
    'cwe_440': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_440.sqlite3'),
    },
    'cwe_276': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_276.sqlite3'),
    },
    'cwe_384': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_384.sqlite3'),
    },
    'cwe_1076': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1076.sqlite3'),
    },
    'cwe_1259': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1259.sqlite3'),
    },
    'cwe_488': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_488.sqlite3'),
    },
    'cwe_1108': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1108.sqlite3'),
    },
    'cwe_463': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_463.sqlite3'),
    },
    'cwe_290': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_290.sqlite3'),
    },
    'cwe_1093': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1093.sqlite3'),
    },
    'cwe_793': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_793.sqlite3'),
    },
    'cwe_134': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_134.sqlite3'),
    },
    'cwe_1319': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1319.sqlite3'),
    },
    'cwe_777': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_777.sqlite3'),
    },
    'cwe_84': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_84.sqlite3'),
    },
    'cwe_471': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_471.sqlite3'),
    },
    'cwe_479': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_479.sqlite3'),
    },
    'cwe_1301': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1301.sqlite3'),
    },
    'cwe_147': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_147.sqlite3'),
    },
    'cwe_704': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_704.sqlite3'),
    },
    'cwe_829': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_829.sqlite3'),
    },
    'cwe_773': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_773.sqlite3'),
    },
    'cwe_489': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_489.sqlite3'),
    },
    'cwe_444': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_444.sqlite3'),
    },
    'cwe_1044': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1044.sqlite3'),
    },
    'cwe_1188': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1188.sqlite3'),
    },
    'cwe_427': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_427.sqlite3'),
    },
    'cwe_359': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_359.sqlite3'),
    },
    'cwe_754': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_754.sqlite3'),
    },
    'cwe_615': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_615.sqlite3'),
    },
    'cwe_120': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_120.sqlite3'),
    },
    'cwe_1192': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1192.sqlite3'),
    },
    'cwe_306': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_306.sqlite3'),
    },
    'cwe_314': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_314.sqlite3'),
    },
    'cwe_117': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_117.sqlite3'),
    },
    'cwe_783': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_783.sqlite3'),
    },
    'cwe_576': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_576.sqlite3'),
    },
    'cwe_245': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_245.sqlite3'),
    },
    'cwe_432': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_432.sqlite3'),
    },
    'cwe_410': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_410.sqlite3'),
    },
    'cwe_197': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_197.sqlite3'),
    },
    'cwe_106': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_106.sqlite3'),
    },
    'cwe_926': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_926.sqlite3'),
    },
    'cwe_1261': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1261.sqlite3'),
    },
    'cwe_1310': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1310.sqlite3'),
    },
    'cwe_651': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_651.sqlite3'),
    },
    'cwe_1314': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1314.sqlite3'),
    },
    'cwe_190': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_190.sqlite3'),
    },
    'cwe_757': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_757.sqlite3'),
    },
    'cwe_198': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_198.sqlite3'),
    },
    'cwe_339': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_339.sqlite3'),
    },
    'cwe_441': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_441.sqlite3'),
    },
    'cwe_1275': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1275.sqlite3'),
    },
    'cwe_397': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_397.sqlite3'),
    },
    'cwe_909': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_909.sqlite3'),
    },
    'cwe_1284': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1284.sqlite3'),
    },
    'cwe_329': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_329.sqlite3'),
    },
    'cwe_638': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_638.sqlite3'),
    },
    'cwe_798': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_798.sqlite3'),
    },
    'cwe_419': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_419.sqlite3'),
    },
    'cwe_315': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_315.sqlite3'),
    },
    'cwe_480': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_480.sqlite3'),
    },
    'cwe_497': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_497.sqlite3'),
    },
    'cwe_910': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_910.sqlite3'),
    },
    'cwe_787': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_787.sqlite3'),
    },
    'cwe_483': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_483.sqlite3'),
    },
    'cwe_375': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_375.sqlite3'),
    },
    'cwe_1323': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1323.sqlite3'),
    },
    'cwe_1095': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1095.sqlite3'),
    },
    'cwe_272': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_272.sqlite3'),
    },
    'cwe_333': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_333.sqlite3'),
    },
    'cwe_571': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_571.sqlite3'),
    },
    'cwe_581': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_581.sqlite3'),
    },
    'cwe_180': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_180.sqlite3'),
    },
    'cwe_693': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_693.sqlite3'),
    },
    'cwe_1114': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1114.sqlite3'),
    },
    'cwe_1126': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1126.sqlite3'),
    },
    'cwe_649': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_649.sqlite3'),
    },
    'cwe_685': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_685.sqlite3'),
    },
    'cwe_1242': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1242.sqlite3'),
    },
    'cwe_474': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_474.sqlite3'),
    },
    'cwe_86': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_86.sqlite3'),
    },
    'cwe_285': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_285.sqlite3'),
    },
    'cwe_385': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_385.sqlite3'),
    },
    'cwe_706': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_706.sqlite3'),
    },
    'cwe_342': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_342.sqlite3'),
    },
    'cwe_391': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_391.sqlite3'),
    },
    'cwe_462': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_462.sqlite3'),
    },
    'cwe_90': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_90.sqlite3'),
    },
    'cwe_1115': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1115.sqlite3'),
    },
    'cwe_99': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_99.sqlite3'),
    },
    'cwe_1116': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1116.sqlite3'),
    },
    'cwe_366': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_366.sqlite3'),
    },
    'cwe_1069': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1069.sqlite3'),
    },
    'cwe_598': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_598.sqlite3'),
    },
    'cwe_1193': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1193.sqlite3'),
    },
    'cwe_211': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_211.sqlite3'),
    },
    'cwe_1103': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1103.sqlite3'),
    },
    'cwe_349': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_349.sqlite3'),
    },
    'cwe_164': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_164.sqlite3'),
    },
    'cwe_172': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_172.sqlite3'),
    },
    'cwe_156': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_156.sqlite3'),
    },
    'cwe_129': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_129.sqlite3'),
    },
    'cwe_1100': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1100.sqlite3'),
    },
    'cwe_1334': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1334.sqlite3'),
    },
    'cwe_269': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_269.sqlite3'),
    },
    'cwe_733': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_733.sqlite3'),
    },
    'cwe_804': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_804.sqlite3'),
    },
    'cwe_319': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_319.sqlite3'),
    },
    'cwe_119': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_119.sqlite3'),
    },
    'cwe_501': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_501.sqlite3'),
    },
    'cwe_1061': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1061.sqlite3'),
    },
    'cwe_238': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_238.sqlite3'),
    },
    'cwe_1296': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1296.sqlite3'),
    },
    'cwe_647': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_647.sqlite3'),
    },
    'cwe_675': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_675.sqlite3'),
    },
    'cwe_281': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_281.sqlite3'),
    },
    'cwe_194': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_194.sqlite3'),
    },
    'cwe_563': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_563.sqlite3'),
    },
    'cwe_927': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_927.sqlite3'),
    },
    'cwe_774': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_774.sqlite3'),
    },
    'cwe_913': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_913.sqlite3'),
    },
    'cwe_508': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_508.sqlite3'),
    },
    'cwe_771': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_771.sqlite3'),
    },
    'cwe_1090': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1090.sqlite3'),
    },
    'cwe_529': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_529.sqlite3'),
    },
    'cwe_799': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_799.sqlite3'),
    },
    'cwe_830': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_830.sqlite3'),
    },
    'cwe_422': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_422.sqlite3'),
    },
    'cwe_1096': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1096.sqlite3'),
    },
    'cwe_572': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_572.sqlite3'),
    },
    'cwe_115': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_115.sqlite3'),
    },
    'cwe_335': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_335.sqlite3'),
    },
    'cwe_121': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_121.sqlite3'),
    },
    'cwe_1109': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1109.sqlite3'),
    },
    'cwe_326': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_326.sqlite3'),
    },
    'cwe_570': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_570.sqlite3'),
    },
    'cwe_766': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_766.sqlite3'),
    },
    'cwe_836': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_836.sqlite3'),
    },
    'cwe_246': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_246.sqlite3'),
    },
    'cwe_1265': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1265.sqlite3'),
    },
    'cwe_511': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_511.sqlite3'),
    },
    'cwe_537': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_537.sqlite3'),
    },
    'cwe_621': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_621.sqlite3'),
    },
    'cwe_118': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_118.sqlite3'),
    },
    'cwe_585': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_585.sqlite3'),
    },
    'cwe_1290': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1290.sqlite3'),
    },
    'cwe_1094': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1094.sqlite3'),
    },
    'cwe_150': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_150.sqlite3'),
    },
    'cwe_434': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_434.sqlite3'),
    },
    'cwe_843': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_843.sqlite3'),
    },
    'cwe_1338': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1338.sqlite3'),
    },
    'cwe_97': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_97.sqlite3'),
    },
    'cwe_379': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_379.sqlite3'),
    },
    'cwe_1311': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1311.sqlite3'),
    },
    'cwe_618': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_618.sqlite3'),
    },
    'cwe_1071': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1071.sqlite3'),
    },
    'cwe_1270': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1270.sqlite3'),
    },
    'cwe_176': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_176.sqlite3'),
    },
    'cwe_212': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_212.sqlite3'),
    },
    'cwe_1233': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1233.sqlite3'),
    },
    'cwe_820': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_820.sqlite3'),
    },
    'cwe_370': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_370.sqlite3'),
    },
    'cwe_1080': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1080.sqlite3'),
    },
    'cwe_105': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_105.sqlite3'),
    },
    'cwe_93': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_93.sqlite3'),
    },
    'cwe_157': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_157.sqlite3'),
    },
    'cwe_309': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_309.sqlite3'),
    },
    'cwe_496': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_496.sqlite3'),
    },
    'cwe_688': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_688.sqlite3'),
    },
    'cwe_1085': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1085.sqlite3'),
    },
    'cwe_922': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_922.sqlite3'),
    },
    'cwe_268': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_268.sqlite3'),
    },
    'cwe_1048': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1048.sqlite3'),
    },
    'cwe_564': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_564.sqlite3'),
    },
    'cwe_173': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_173.sqlite3'),
    },
    'cwe_435': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_435.sqlite3'),
    },
    'cwe_196': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_196.sqlite3'),
    },
    'cwe_135': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_135.sqlite3'),
    },
    'cwe_593': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_593.sqlite3'),
    },
    'cwe_525': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_525.sqlite3'),
    },
    'cwe_1059': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1059.sqlite3'),
    },
    'cwe_540': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_540.sqlite3'),
    },
    'cwe_243': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_243.sqlite3'),
    },
    'cwe_141': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_141.sqlite3'),
    },
    'cwe_608': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_608.sqlite3'),
    },
    'cwe_642': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_642.sqlite3'),
    },
    'cwe_509': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_509.sqlite3'),
    },
    'cwe_1007': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1007.sqlite3'),
    },
    'cwe_1102': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1102.sqlite3'),
    },
    'cwe_161': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_161.sqlite3'),
    },
    'cwe_1050': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1050.sqlite3'),
    },
    'cwe_1045': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1045.sqlite3'),
    },
    'cwe_407': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_407.sqlite3'),
    },
    'cwe_842': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_842.sqlite3'),
    },
    'cwe_1064': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1064.sqlite3'),
    },
    'cwe_203': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_203.sqlite3'),
    },
    'cwe_1304': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1304.sqlite3'),
    },
    'cwe_431': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_431.sqlite3'),
    },
    'cwe_179': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_179.sqlite3'),
    },
    'cwe_182': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_182.sqlite3'),
    },
    'cwe_138': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_138.sqlite3'),
    },
    'cwe_1328': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1328.sqlite3'),
    },
    'cwe_1330': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1330.sqlite3'),
    },
    'cwe_695': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_695.sqlite3'),
    },
    'cwe_279': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_279.sqlite3'),
    },
    'cwe_622': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_622.sqlite3'),
    },
    'cwe_670': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_670.sqlite3'),
    },
    'cwe_1245': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1245.sqlite3'),
    },
    'cwe_158': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_158.sqlite3'),
    },
    'cwe_414': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_414.sqlite3'),
    },
    'cwe_210': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_210.sqlite3'),
    },
    'cwe_797': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_797.sqlite3'),
    },
    'cwe_1074': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1074.sqlite3'),
    },
    'cwe_1257': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1257.sqlite3'),
    },
    'cwe_506': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_506.sqlite3'),
    },
    'cwe_1113': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1113.sqlite3'),
    },
    'cwe_791': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_791.sqlite3'),
    },
    'cwe_167': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_167.sqlite3'),
    },
    'cwe_186': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_186.sqlite3'),
    },
    'cwe_1318': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1318.sqlite3'),
    },
    'cwe_464': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_464.sqlite3'),
    },
    'cwe_763': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_763.sqlite3'),
    },
    'cwe_328': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_328.sqlite3'),
    },
    'cwe_575': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_575.sqlite3'),
    },
    'cwe_473': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_473.sqlite3'),
    },
    'cwe_668': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_668.sqlite3'),
    },
    'cwe_250': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_250.sqlite3'),
    },
    'cwe_201': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_201.sqlite3'),
    },
    'cwe_352': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_352.sqlite3'),
    },
    'cwe_586': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_586.sqlite3'),
    },
    'cwe_127': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_127.sqlite3'),
    },
    'cwe_626': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_626.sqlite3'),
    },
    'cwe_241': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_241.sqlite3'),
    },
    'cwe_466': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_466.sqlite3'),
    },
    'cwe_299': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_299.sqlite3'),
    },
    'cwe_600': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_600.sqlite3'),
    },
    'cwe_402': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_402.sqlite3'),
    },
    'cwe_1022': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1022.sqlite3'),
    },
    'cwe_1191': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1191.sqlite3'),
    },
    'cwe_918': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_918.sqlite3'),
    },
    'cwe_1324': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1324.sqlite3'),
    },
    'cwe_1112': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1112.sqlite3'),
    },
    'cwe_920': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_920.sqlite3'),
    },
    'cwe_390': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_390.sqlite3'),
    },
    'cwe_236': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_236.sqlite3'),
    },
    'cwe_1293': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1293.sqlite3'),
    },
    'cwe_1037': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1037.sqlite3'),
    },
    'cwe_770': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_770.sqlite3'),
    },
    'cwe_521': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_521.sqlite3'),
    },
    'cwe_220': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_220.sqlite3'),
    },
    'cwe_266': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_266.sqlite3'),
    },
    'cwe_602': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_602.sqlite3'),
    },
    'cwe_111': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_111.sqlite3'),
    },
    'cwe_192': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_192.sqlite3'),
    },
    'cwe_311': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_311.sqlite3'),
    },
    'cwe_175': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_175.sqlite3'),
    },
    'cwe_573': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_573.sqlite3'),
    },
    'cwe_1052': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1052.sqlite3'),
    },
    'cwe_334': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_334.sqlite3'),
    },
    'cwe_459': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_459.sqlite3'),
    },
    'cwe_780': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_780.sqlite3'),
    },
    'cwe_547': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_547.sqlite3'),
    },
    'cwe_560': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_560.sqlite3'),
    },
    'cwe_789': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_789.sqlite3'),
    },
    'cwe_676': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_676.sqlite3'),
    },
    'cwe_543': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_543.sqlite3'),
    },
    'cwe_1299': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1299.sqlite3'),
    },
    'cwe_636': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_636.sqlite3'),
    },
    'cwe_823': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_823.sqlite3'),
    },
    'cwe_367': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_367.sqlite3'),
    },
    'cwe_239': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_239.sqlite3'),
    },
    'cwe_1286': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1286.sqlite3'),
    },
    'cwe_1294': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1294.sqlite3'),
    },
    'cwe_528': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_528.sqlite3'),
    },
    'cwe_539': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_539.sqlite3'),
    },
    'cwe_166': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_166.sqlite3'),
    },
    'cwe_353': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_353.sqlite3'),
    },
    'cwe_1110': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1110.sqlite3'),
    },
    'cwe_805': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_805.sqlite3'),
    },
    'cwe_561': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_561.sqlite3'),
    },
    'cwe_486': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_486.sqlite3'),
    },
    'cwe_825': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_825.sqlite3'),
    },
    'cwe_1053': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1053.sqlite3'),
    },
    'cwe_562': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_562.sqlite3'),
    },
    'cwe_567': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_567.sqlite3'),
    },
    'cwe_467': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_467.sqlite3'),
    },
    'cwe_404': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_404.sqlite3'),
    },
    'cwe_1047': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1047.sqlite3'),
    },
    'cwe_356': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_356.sqlite3'),
    },
    'cwe_1025': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1025.sqlite3'),
    },
    'cwe_386': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_386.sqlite3'),
    },
    'cwe_1078': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1078.sqlite3'),
    },
    'cwe_477': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_477.sqlite3'),
    },
    'cwe_708': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_708.sqlite3'),
    },
    'cwe_671': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_671.sqlite3'),
    },
    'cwe_507': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_507.sqlite3'),
    },
    'cwe_667': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_667.sqlite3'),
    },
    'cwe_756': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_756.sqlite3'),
    },
    'cwe_96': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_96.sqlite3'),
    },
    'cwe_122': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_122.sqlite3'),
    },
    'cwe_822': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_822.sqlite3'),
    },
    'cwe_193': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_193.sqlite3'),
    },
    'cwe_360': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_360.sqlite3'),
    },
    'cwe_420': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_420.sqlite3'),
    },
    'cwe_760': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_760.sqlite3'),
    },
    'cwe_177': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_177.sqlite3'),
    },
    'cwe_231': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_231.sqlite3'),
    },
    'cwe_82': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_82.sqlite3'),
    },
    'cwe_288': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_288.sqlite3'),
    },
    'cwe_767': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_767.sqlite3'),
    },
    'cwe_322': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_322.sqlite3'),
    },
    'cwe_259': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_259.sqlite3'),
    },
    'cwe_1223': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1223.sqlite3'),
    },
    'cwe_382': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_382.sqlite3'),
    },
    'cwe_781': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_781.sqlite3'),
    },
    'cwe_107': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_107.sqlite3'),
    },
    'cwe_365': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_365.sqlite3'),
    },
    'cwe_1224': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1224.sqlite3'),
    },
    'cwe_613': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_613.sqlite3'),
    },
    'cwe_665': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_665.sqlite3'),
    },
    'cwe_1051': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1051.sqlite3'),
    },
    'cwe_1268': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1268.sqlite3'),
    },
    'cwe_597': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_597.sqlite3'),
    },
    'cwe_498': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_498.sqlite3'),
    },
    'cwe_159': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_159.sqlite3'),
    },
    'cwe_298': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_298.sqlite3'),
    },
    'cwe_620': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_620.sqlite3'),
    },
    'cwe_1251': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1251.sqlite3'),
    },
    'cwe_624': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_624.sqlite3'),
    },
    'cwe_205': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_205.sqlite3'),
    },
    'cwe_1209': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1209.sqlite3'),
    },
    'cwe_123': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_123.sqlite3'),
    },
    'cwe_487': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_487.sqlite3'),
    },
    'cwe_691': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_691.sqlite3'),
    },
    'cwe_526': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_526.sqlite3'),
    },
    'cwe_215': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_215.sqlite3'),
    },
    'cwe_87': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_87.sqlite3'),
    },
    'cwe_1043': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1043.sqlite3'),
    },
    'cwe_1256': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1256.sqlite3'),
    },
    'cwe_1252': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1252.sqlite3'),
    },
    'cwe_640': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_640.sqlite3'),
    },
    'cwe_168': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_168.sqlite3'),
    },
    'cwe_83': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_83.sqlite3'),
    },
    'cwe_612': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_612.sqlite3'),
    },
    'cwe_768': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_768.sqlite3'),
    },
    'cwe_1297': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1297.sqlite3'),
    },
    'cwe_527': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_527.sqlite3'),
    },
    'cwe_500': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_500.sqlite3'),
    },
    'cwe_468': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_468.sqlite3'),
    },
    'cwe_1321': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1321.sqlite3'),
    },
    'cwe_294': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_294.sqlite3'),
    },
    'cwe_1234': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1234.sqlite3'),
    },
    'cwe_785': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_785.sqlite3'),
    },
    'cwe_110': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_110.sqlite3'),
    },
    'cwe_235': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_235.sqlite3'),
    },
    'cwe_341': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_341.sqlite3'),
    },
    'cwe_532': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_532.sqlite3'),
    },
    'cwe_492': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_492.sqlite3'),
    },
    'cwe_551': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_551.sqlite3'),
    },
    'cwe_148': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_148.sqlite3'),
    },
    'cwe_806': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_806.sqlite3'),
    },
    'cwe_664': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_664.sqlite3'),
    },
    'cwe_226': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_226.sqlite3'),
    },
    'cwe_430': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_430.sqlite3'),
    },
    'cwe_656': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_656.sqlite3'),
    },
    'cwe_703': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_703.sqlite3'),
    },
    'cwe_1189': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1189.sqlite3'),
    },
    'cwe_1038': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1038.sqlite3'),
    },
    'cwe_924': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_924.sqlite3'),
    },
    'cwe_374': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_374.sqlite3'),
    },
    'cwe_1274': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1274.sqlite3'),
    },
    'cwe_69': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_69.sqlite3'),
    },
    'cwe_1023': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1023.sqlite3'),
    },
    'cwe_400': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_400.sqlite3'),
    },
    'cwe_1239': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1239.sqlite3'),
    },
    'cwe_330': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_330.sqlite3'),
    },
    'cwe_149': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_149.sqlite3'),
    },
    'cwe_433': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_433.sqlite3'),
    },
    'cwe_666': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_666.sqlite3'),
    },
    'cwe_187': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_187.sqlite3'),
    },
    'cwe_574': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_574.sqlite3'),
    },
    'cwe_1073': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1073.sqlite3'),
    },
    'cwe_337': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_337.sqlite3'),
    },
    'cwe_784': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_784.sqlite3'),
    },
    'cwe_202': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_202.sqlite3'),
    },
    'cwe_611': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_611.sqlite3'),
    },
    'cwe_610': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_610.sqlite3'),
    },
    'cwe_641': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_641.sqlite3'),
    },
    'cwe_772': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_772.sqlite3'),
    },
    'cwe_587': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_587.sqlite3'),
    },
    'cwe_392': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_392.sqlite3'),
    },
    'cwe_415': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_415.sqlite3'),
    },
    'cwe_637': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_637.sqlite3'),
    },
    'cwe_470': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_470.sqlite3'),
    },
    'cwe_546': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_546.sqlite3'),
    },
    'cwe_643': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_643.sqlite3'),
    },
    'cwe_681': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_681.sqlite3'),
    },
    'cwe_277': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_277.sqlite3'),
    },
    'cwe_1235': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1235.sqlite3'),
    },
    'cwe_1058': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1058.sqlite3'),
    },
    'cwe_91': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_91.sqlite3'),
    },
    'cwe_761': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_761.sqlite3'),
    },
    'cwe_1088': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1088.sqlite3'),
    },
    'cwe_145': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_145.sqlite3'),
    },
    'cwe_162': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_162.sqlite3'),
    },
    'cwe_303': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_303.sqlite3'),
    },
    'cwe_221': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_221.sqlite3'),
    },
    'cwe_428': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_428.sqlite3'),
    },
    'cwe_707': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_707.sqlite3'),
    },
    'cwe_831': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_831.sqlite3'),
    },
    'cwe_95': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_95.sqlite3'),
    },
    'cwe_346': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_346.sqlite3'),
    },
    'cwe_1089': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1089.sqlite3'),
    },
    'cwe_318': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_318.sqlite3'),
    },
    'cwe_862': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_862.sqlite3'),
    },
    'cwe_383': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_383.sqlite3'),
    },
    'cwe_253': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_253.sqlite3'),
    },
    'cwe_293': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_293.sqlite3'),
    },
    'cwe_455': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_455.sqlite3'),
    },
    'cwe_522': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_522.sqlite3'),
    },
    'cwe_566': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_566.sqlite3'),
    },
    'cwe_104': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_104.sqlite3'),
    },
    'cwe_607': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_607.sqlite3'),
    },
    'cwe_301': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_301.sqlite3'),
    },
    'cwe_214': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_214.sqlite3'),
    },
    'cwe_77': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_77.sqlite3'),
    },
    'cwe_499': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_499.sqlite3'),
    },
    'cwe_112': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_112.sqlite3'),
    },
    'cwe_207': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_207.sqlite3'),
    },
    'cwe_494': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_494.sqlite3'),
    },
    'cwe_524': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_524.sqlite3'),
    },
    'cwe_558': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_558.sqlite3'),
    },
    'cwe_240': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_240.sqlite3'),
    },
    'cwe_565': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_565.sqlite3'),
    },
    'cwe_674': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_674.sqlite3'),
    },
    'cwe_1119': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1119.sqlite3'),
    },
    'cwe_130': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_130.sqlite3'),
    },
    'cwe_478': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_478.sqlite3'),
    },
    'cwe_351': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_351.sqlite3'),
    },
    'cwe_1278': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1278.sqlite3'),
    },
    'cwe_779': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_779.sqlite3'),
    },
    'cwe_232': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_232.sqlite3'),
    },
    'cwe_191': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_191.sqlite3'),
    },
    'cwe_1295': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1295.sqlite3'),
    },
    'cwe_1221': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1221.sqlite3'),
    },
    'cwe_1283': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1283.sqlite3'),
    },
    'cwe_287': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_287.sqlite3'),
    },
    'cwe_523': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_523.sqlite3'),
    },
    'cwe_372': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_372.sqlite3'),
    },
    'cwe_616': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_616.sqlite3'),
    },
    'cwe_863': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_863.sqlite3'),
    },
    'cwe_1127': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1127.sqlite3'),
    },
    'cwe_1176': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1176.sqlite3'),
    },
    'cwe_233': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_233.sqlite3'),
    },
    'cwe_278': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_278.sqlite3'),
    },
    'cwe_256': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_256.sqlite3'),
    },
    'cwe_908': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_908.sqlite3'),
    },
    'cwe_491': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_491.sqlite3'),
    },
    'cwe_943': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_943.sqlite3'),
    },
    'cwe_794': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_794.sqlite3'),
    },
    'cwe_113': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_113.sqlite3'),
    },
    'cwe_274': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_274.sqlite3'),
    },
    'cwe_109': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_109.sqlite3'),
    },
    'cwe_291': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_291.sqlite3'),
    },
    'cwe_1254': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1254.sqlite3'),
    },
    'cwe_209': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_209.sqlite3'),
    },
    'cwe_697': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_697.sqlite3'),
    },
    'cwe_81': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_81.sqlite3'),
    },
    'cwe_229': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_229.sqlite3'),
    },
    'cwe_396': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_396.sqlite3'),
    },
    'cwe_143': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_143.sqlite3'),
    },
    'cwe_940': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_940.sqlite3'),
    },
    'cwe_1063': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1063.sqlite3'),
    },
    'cwe_1111': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1111.sqlite3'),
    },
    'cwe_694': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_694.sqlite3'),
    },
    'cwe_1241': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1241.sqlite3'),
    },
    'cwe_308': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_308.sqlite3'),
    },
    'cwe_1269': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1269.sqlite3'),
    },
    'cwe_450': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_450.sqlite3'),
    },
    'cwe_1070': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1070.sqlite3'),
    },
    'cwe_1173': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1173.sqlite3'),
    },
    'cwe_786': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_786.sqlite3'),
    },
    'cwe_778': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_778.sqlite3'),
    },
    'cwe_1082': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1082.sqlite3'),
    },
    'cwe_832': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_832.sqlite3'),
    },
    'cwe_1231': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1231.sqlite3'),
    },
    'cwe_614': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_614.sqlite3'),
    },
    'cwe_426': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_426.sqlite3'),
    },
    'cwe_580': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_580.sqlite3'),
    },
    'cwe_941': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_941.sqlite3'),
    },
    'cwe_437': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_437.sqlite3'),
    },
    'cwe_625': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_625.sqlite3'),
    },
    'cwe_552': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_552.sqlite3'),
    },
    'cwe_401': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_401.sqlite3'),
    },
    'cwe_436': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_436.sqlite3'),
    },
    'cwe_796': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_796.sqlite3'),
    },
    'cwe_408': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_408.sqlite3'),
    },
    'cwe_939': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_939.sqlite3'),
    },
    'cwe_645': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_645.sqlite3'),
    },
    'cwe_673': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_673.sqlite3'),
    },
    'cwe_1057': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1057.sqlite3'),
    },
    'cwe_252': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_252.sqlite3'),
    },
    'cwe_1315': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1315.sqlite3'),
    },
    'cwe_1125': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_1125.sqlite3'),
    },
    'cwe_75': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_75.sqlite3'),
    },
    'cwe_151': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_151.sqlite3'),
    },
    'cwe_126': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_126.sqlite3'),
    },
    'cwe_295': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_295.sqlite3'),
    },
    'cwe_none': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CWE_DATABASES_DIR, 'cwe_none.sqlite3'),
    },

}