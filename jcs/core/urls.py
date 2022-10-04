from django.urls import path

from core.views import Inicio
from core.views import vacio
from core.views import stock
urlpatterns = [

    path('inicio/', Inicio),
    path('vacio/', vacio),
    path('stock/', stock),
]