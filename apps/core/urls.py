from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'municipios', views.I012MunicipioList)
router.register(r'uf', views.I011UfViewSet)
router.register(r'municipio-list', views.ViewMunicipioList)
router.register(r'empresa', views.I002EmpresaViewSet)
router.register(r'filais', views.I005FilialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]