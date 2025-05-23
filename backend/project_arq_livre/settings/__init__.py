import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

# Define qual arquivo de settings usar baseado na variável de ambiente DJANGO_SETTINGS_MODULE
# Em desenvolvimento, você pode definir DJANGO_SETTINGS_MODULE=project_arq_livre.settings.dev
# Em produção, DJANGO_SETTINGS_MODULE=project_arq_livre.settings.prod
SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE', 'project_arq_livre.settings.dev')

if SETTINGS_MODULE == 'project_arq_livre.settings.dev':
    from .dev import *
elif SETTINGS_MODULE == 'project_arq_livre.settings.prod':
    from .prod import *
else:
    from .base import * # Fallback para base se nada for definido