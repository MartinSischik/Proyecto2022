from django.urls import path

from core.views import Inicio

urlpatterns = [

    path('inicio/', Inicio),

]