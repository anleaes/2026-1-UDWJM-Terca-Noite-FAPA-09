from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('api/', include('core.urls_api', namespace='api')),
    path('usuarios/', include('users.urls_web', namespace='users_web')),
    path('locais/', include('locais.urls', namespace='locais')),
    path('alocacoes/', include('alocacao.urls_web', namespace='alocacao_web')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

