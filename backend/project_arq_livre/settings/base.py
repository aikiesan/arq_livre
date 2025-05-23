import os
import environ # Para gerenciar variáveis de ambiente

# Configurações iniciais do django-environ
env = environ.Env(
    # Defina o tipo de cada variável de ambiente e seu valor padrão
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'INSECURE_DEFAULT_KEY_DO_NOT_USE_IN_PROD'),
    DATABASE_URL=(str, 'sqlite:///db.sqlite3'),
    ALLOWED_HOSTS=(list, ['127.0.0.1', 'localhost']),
)

# Caminho base do projeto (onde está o manage.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carrega variáveis de ambiente do .env
# Isso assume que o .env está na raiz do projeto (backend/.env)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# --- Configurações Core ---
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# --- Aplicativos (Apps) ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Seus aplicativos personalizados:
    'apps.core',
    'apps.content',
    'apps.users',

    # Outras libs (se precisar)
    'markdown', # Para renderizar markdown
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

ROOT_URLCONF = 'project_arq_livre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Adiciona a pasta global de templates
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

WSGI_APPLICATION = 'project_arq_livre.wsgi.application'
ASGI_APPLICATION = 'project_arq_livre.asgi.application' # Para futuro suporte a Websockets/Async

# --- Banco de Dados ---
DATABASES = {
    'default': env.db(), # Lê a URL do DB do .env (DATABASE_URL)
}

# --- Autenticação ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# --- Internacionalização ---
LANGUAGE_CODE = 'pt-br' # Brasil
TIME_ZONE = 'America/Sao_Paulo' # Fuso horário do Brasil
USE_I18N = True # Suporte a internacionalização
USE_TZ = True # Suporte a fusos horários

# --- Arquivos Estáticos (CSS, JS, Imagens) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected') # Onde Django vai coletar os arquivos estáticos para produção
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # Adiciona a pasta global de estáticos
]

# --- Arquivos de Mídia (Uploads de Usuários) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Onde os arquivos de mídia serão armazenados

# --- Outras Configurações ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Define o tipo de chave primária padrão