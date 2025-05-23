from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclua as URLs do seu aplicativo 'core'
    path('', include('apps.core.urls')),
    # Mais tarde, você adicionará as URLs para 'content', 'users', etc.
    # path('conteudo/', include('apps.content.urls')),
    # path('usuarios/', include('apps.users.urls')),
]

# Configurações para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)