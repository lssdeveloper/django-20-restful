from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from localizacoes.api.viewsets import LocalizacaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'localizacoes', LocalizacaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


