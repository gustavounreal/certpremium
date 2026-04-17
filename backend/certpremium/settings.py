import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

#dbuild paths
BASE_DIR = Path(__file__).resolve().parent.parent

#Carrega variáveis do .env
load_dotenv()

# ==== SEGURANÇA: Nunca hardcorad secrets! ====
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-apenas-para-build")
DEBUG = os.getenv("DEBUG", "0") == "1"

#Hosts permitidos (ajuste para seu domínio)
ALLOWED_HOSTS = [

    "45.32.174.51",
    "localhost",
    "127.0.0.1",
    "api.certpremium.com.br",
        ]

#=== APPS INSTALADOS ===

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    # Local
    'core',
]


# === MIDDLEWARE (ordem importa!) ===
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # PRIMEIRO!
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'certpremium.urls'

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

WSGI_APPLICATION = 'certpremium.wsgi.application'


# === STATICS FILES (CSS, JS, IMAGENS) ===
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# === BANCO DE DADOS (via Docker Compose) ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cert_database',
        'USER': 'cert_user',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'db',  # Nome do serviço no docker-compose
        'PORT': '5432',
    }
}

# === PASSWORD VALIDATORS ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === INTERNACIONALIZAÇÃO ===
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# === STATIC FILES ===
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === CUSTOM USER MODEL ===
AUTH_USER_MODEL = 'core.CustomUser'

# === DRF: Rate Limiting (Anti-DoS/Brute-Force) ===
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '30/minute',   # Limita ataques não autenticados
        'user': '100/minute'  # Usuários logados têm mais margem
    }
}

# === JWT: Tokens com vida curta (Least Privilege) ===
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
}

# === CORS: Controle de Origens ===
CORS_ALLOWED_ORIGINS = [
    "https://certpremium.com.br",
    "https://www.certpremium.com.br",
]

if DEBUG:
    CORS_ALLOWED_ORIGINS += [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

CORS_ALLOW_HEADERS = [
    'accept',
    'authorization',
    'content-type',
    'origin',
    'x-requested-with',
]

# === SECURITY HEADERS ===
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Em produção (HTTPS), ative também:
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# === LOGGING ESTRUTURADO (JSON para SIEM) ===
# No CI, só usa console. Em produção, cria diretório de logs se não existir
LOG_DIR = Path('/app/logs')
if not DEBUG and LOG_DIR.parent.exists():  # Só tenta criar em produção
    LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.security': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'certpremium': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    },
}

# Adiciona file handler apenas se o diretório existir (produção)
if LOG_DIR.exists():
    LOGGING['handlers']['file'] = {
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': str(LOG_DIR / 'api.json'),
        'maxBytes': 5 * 1024 * 1024,
        'backupCount': 3,
        'formatter': 'json',
    }
    LOGGING['loggers']['django.security']['handlers'].append('file')
    LOGGING['loggers']['certpremium']['handlers'].append('file')


