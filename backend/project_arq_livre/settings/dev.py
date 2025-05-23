from .base import *

# Configurações específicas de desenvolvimento
DEBUG = env('DEBUG') # Lê do .env
ALLOWED_HOSTS = env('ALLOWED_HOSTS') # Lê do .env

# Outras configurações de desenvolvimento (ex: logging, debug toolbar)
# INSTALLED_APPS += [
#     'debug_toolbar',
# ]
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
# INTERNAL_IPS = [
#     '127.0.0.1',
# ]