from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'productos', views.ListaProductos)
router.register(r'tipo_productos', views.ListaTipoProductos)

urlpatterns = [
    path('vista/', include(router.urls)),
]