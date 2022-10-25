
from django.urls import path

from core import views

urlpatterns = [

    path('inicio/',views.Inicio, name='Inicio'),
    path('vacio/',views.vacio, name='vacio'),
    path('stock/',views.stock, name='stock'),
    path('Cargastock/',views.Cargastock, name='Cargastock'),
    path('CargaGrano/',views.CargaGrano, name='CargaGrano'),
]