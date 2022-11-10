
from django.urls import path

from core import views
from core.views import*
from login.views import LoginFormView
urlpatterns = [

    path('inicio/',views.Inicio, name='Inicio'),
    path('home/',views.home, name='home'),
    path('stock/',views.stock, name='stock'),
    path('login/',LoginFormView.as_view(), name='login'),
    path('CargaQuimico/add/',CargaQuimico.as_view(), name='CargaQuimico'),
    path('EditQuimico/edit/<int:pk>/',EditQuimico.as_view(), name='EditQuimico'),
    path('DeleteQuimico/delete/<int:pk>/',DeleteQuimico.as_view(), name='DeleteQuimico'),
    path('CargaGrano/add/',CargaGrano.as_view(), name='CargaGrano'),
    path('EditGrano/edit/<int:pk>/',EditGrano.as_view(), name='EditGrano'),
    path('DeleteGrano/delete/<int:pk>/',DeleteGrano.as_view(), name='DeleteGrano'),
    path('CargaCateQui/add/',CatQuimiCreateview.as_view(), name='CargaCateQui'),
    path('CatQuimiEditview/edit/<int:pk>/',CatQuimiEditview.as_view(), name='CatQuimiEditview'),
    path('DeleteQuimiCate/delete/<int:pk>/',DeleteQuimiCate.as_view(), name='DeleteQuimiCate'),
    path('CargaParcela/add/',CargaParcela.as_view(), name='CargaParcela'),
    path('EditParcela/edit/<int:pk>/',EditParcela.as_view(), name='EditParcela'),
    path('DeleteParcela/delete/<int:pk>/',DeleteParcela.as_view(), name='DeleteParcela'),
]