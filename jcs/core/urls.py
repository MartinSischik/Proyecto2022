
from django.urls import path

from core import views
from core.Sale.views import SaleCreateView
from core.views import*
from login.views import LoginFormView
from django.contrib.auth.views import*
urlpatterns = [

    path('inicio/',views.Inicio, name='inicio'),
    path('home/',views.home, name='home'),
    # path('stock/',views.stock, name='stock'),
    path('stock2/',views.stock2, name='stock2'),
    path('Entregas_Stock/',views.Entregas_Stock, name='Entregas_Stock'),
    path('Parcela/',views.Parcela, name='Parcela'),
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
    # Trabajos
    path('CargaTrabajo/add/',CargaTrabajo.as_view(), name='CargaTrabajo'),
    path('EditTrabajo/edit/<int:pk>/',EditTrabajo.as_view(), name='EditTrabajo'),
    path('DeleteTrabajo/delete/<int:pk>/',DeleteTrabajo.as_view(), name='DeleteTrabajo'),
    # trabajo prueba
    path('SaleCreateView/add/',SaleCreateView.as_view(), name='SaleCreateView'),

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
    path('CargaProveedor/add/',CargaProveedor.as_view(), name='CargaProveedor'),
    path('EditProveedor/edit/<int:pk>/',EditProveedor.as_view(), name='EditProveedor'),
    path('DeleteProveedor/delete/<int:pk>/',DeleteProveedor.as_view(), name='DeleteProveedor'),
    # Produccion
    path('CargaProduccion/add/',CargaProduccion.as_view(), name='CargaProduccion'),
    path('EditProduccion/edit/<int:pk>/',EditProduccion.as_view(), name='EditProduccion'),
    path('DeleteProduccion/delete/<int:pk>/',DeleteProduccion.as_view(), name='DeleteProduccion'),
]