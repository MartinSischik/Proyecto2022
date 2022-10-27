
from django.urls import path

from core import views
from core.views import*
urlpatterns = [

    path('inicio/',views.Inicio, name='Inicio'),
    path('home/',views.home, name='home'),
    path('stock/',views.stock, name='stock'),
    path('Cargastock/add/',Cargastock.as_view(), name='Cargastock'),
    path('CargaGrano/',views.CargaGrano, name='CargaGrano'),
    path('CargaCateQui/add/',CatQuimiCreateview.as_view(), name='CargaCateQui'),
]