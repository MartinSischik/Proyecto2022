
from django.urls import path

from core import views
from core.views import*
from login.views import LoginFormView
from django.contrib.auth.views import*
urlpatterns = [

    path('inicio/',views.Inicio, name='Inicio'),
    path('home/',views.home, name='home'),
    path('stock/',views.stock, name='stock'),
    path('Entregas_Stock/',views.Entregas_Stock, name='Entregas_Stock'),
    path('ListaCliente/',views.ListaCliente.as_view(), name='ListaCliente'),
    path('ListaProveedor/',views.ListaProveedor.as_view(), name='ListaProveedor'),
    # login
    path('login/',LoginFormView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    # Agroquimicos
    path('CargaQuimico/add/',CargaQuimico.as_view(), name='CargaQuimico'),
    path('EditQuimico/edit/<int:pk>/',EditQuimico.as_view(), name='EditQuimico'),
    path('DeleteQuimico/delete/<int:pk>/',DeleteQuimico.as_view(), name='DeleteQuimico'),
    # Granos
    path('CargaGrano/add/',CargaGrano.as_view(), name='CargaGrano'),
    path('EditGrano/edit/<int:pk>/',EditGrano.as_view(), name='EditGrano'),
    path('DeleteGrano/delete/<int:pk>/',DeleteGrano.as_view(), name='DeleteGrano'),
    # Categoria Agroquimicos
    path('CargaCateQui/add/',CatQuimiCreateview.as_view(), name='CargaCateQui'),
    path('CatQuimiEditview/edit/<int:pk>/',CatQuimiEditview.as_view(), name='CatQuimiEditview'),
    path('DeleteQuimiCate/delete/<int:pk>/',DeleteQuimiCate.as_view(), name='DeleteQuimiCate'),
    # Parcelas
    path('CargaParcela/add/',CargaParcela.as_view(), name='CargaParcela'),
    path('EditParcela/edit/<int:pk>/',EditParcela.as_view(), name='EditParcela'),
    path('DeleteParcela/delete/<int:pk>/',DeleteParcela.as_view(), name='DeleteParcela'),
    # Camiones
    path('CargaCamion/add/',CargaCamion.as_view(), name='CargaCamion'),
    path('EditCamion/edit/<int:pk>/',EditCamion.as_view(), name='EditCamion'),
    path('DeleteCamion/delete/<int:pk>/',DeleteCamion.as_view(), name='DeleteCamion'),
    # Entregas
    path('CargaEntregas/add/',CargaEntregas.as_view(), name='CargaEntregas'),
    path('EditEntregas/edit/<int:pk>/',EditEntregas.as_view(), name='EditEntregas'),
    path('DeleteEntregas/delete/<int:pk>/',DeleteEntregas.as_view(), name='DeleteEntregas'),
    #Clientes
    path('CargaCliente/add/',CargaCliente.as_view(), name='CargaCliente'),
    path('EditCliente/edit/<int:pk>/',EditCliente.as_view(), name='EditCliente'),
    path('DeleteCliente/delete/<int:pk>/',DeleteCliente.as_view(), name='DeleteCliente'),
    # Proveedores
    path('CargaCliente/add/',CargaCliente.as_view(), name='CargaCliente'),
    path('EditCliente/edit/<int:pk>/',EditCliente.as_view(), name='EditCliente'),
    path('DeleteCliente/delete/<int:pk>/',DeleteCliente.as_view(), name='DeleteCliente'),
]