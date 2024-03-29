from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'empleados', views.ListaEmpleados)

urlpatterns = [
    path('vista/', include(router.urls)),
]