from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'clientes', views.ListaClientes)

app_name = 'clientes'

urlpatterns = [
    path('vista/', include(router.urls)),
    path('vista/frecuente/lista/', views.ListaClientesFrecuentes.as_view(), name='frequent_clients-list'),
    path('vista/frecuente/crear/', views.CrearClienteFrecuentes.as_view(), name='frequent_clients-create'),
]