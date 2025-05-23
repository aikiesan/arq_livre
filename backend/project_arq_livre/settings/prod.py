from .base import *

# Configurações específicas de produção
DEBUG = False # Sempre False em produção!
ALLOWED_HOSTS = env('ALLOWED_HOSTS') # Leia os hosts permitidos do .env

# Configurações de segurança para produção
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True # Habilite se você estiver usando HTTPS (altamente recomendado!)
SECURE_HSTS_SECONDS = 31536000 # HSTS habilitado por 1 ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY' # Previne Clickjacking

# Configurações de log para produção
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# Outras configurações de produção (ex: cache, email backend)
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }