
from django.urls import path

from core import views
from core.Sale.views import *
from core.views import *
from login.views import LoginFormView
from usuario.views import *
from django.contrib.auth.views import *
urlpatterns = [

    path('inicio/', views.Inicio, name='inicio'),
    path('home/', views.home, name='home'),
    # path('stock/',views.stock, name='stock'),
    path('stock2/', views.stock2, name='stock2'),
    path('auditoria/', views.auditoria, name='auditoria'),
    #     path('eliminarauditoria/', views.eliminarauditoria, name='eliminarauditoria'),

    path('ListaTrabajo/', views.ListaTrabajo, name='ListaTrabajo'),
    path('ListaDetalleTrabajo/<int:id_trabajo>/',
         views.ListaDetalleTrabajo, name='ListaDetalleTrabajo'),

    path('Entregas_Stock/', views.Entregas_Stock, name='Entregas_Stock'),
    path('Parcela/', views.Parcela, name='Parcela'),
    path('ListaCliente/', views.ListaCliente.as_view(), name='ListaCliente'),
    path('ListaProveedor/', views.ListaProveedor.as_view(), name='ListaProveedor'),
    # login
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # usuarios
    path('UserListView/', UserListView.as_view(), name='UserListView'),
    path('UserCreateView/add/', UserCreateView.as_view(), name='UserCreateView'),
    path('UserDeleteView/delete/<int:pk>/',
         UserDeleteView.as_view(), name='UserDeleteView'),
    path('UserUpdateView/edit/<int:pk>/',
         UserUpdateView.as_view(), name='UserUpdateView'),
    path('ErrorUsuario/', views.ErrorUsuario, name='ErrorUsuario'),
    # Agroquimicos
    path('CargaQuimico/add/', CargaQuimico.as_view(), name='CargaQuimico'),
    path('SumaQuimico/add/', SumaQuimico.as_view(), name='SumaQuimico'),
    path('EditQuimico/edit/<int:pk>/', EditQuimico.as_view(), name='EditQuimico'),
    path('DeleteQuimico/delete/<int:pk>/',
         DeleteQuimico.as_view(), name='DeleteQuimico'),
    # Granos
    path('CargaGrano/add/', CargaGrano.as_view(), name='CargaGrano'),
    path('EditGrano/edit/<int:pk>/', EditGrano.as_view(), name='EditGrano'),
    path('DeleteGrano/delete/<int:pk>/',
         DeleteGrano.as_view(), name='DeleteGrano'),
    # Categoria Agroquimicos
    path('CargaCateQui/add/', CatQuimiCreateview.as_view(), name='CargaCateQui'),
    path('CatQuimiEditview/edit/<int:pk>/',
         CatQuimiEditview.as_view(), name='CatQuimiEditview'),
    path('DeleteQuimiCate/delete/<int:pk>/',
         DeleteQuimiCate.as_view(), name='DeleteQuimiCate'),
    # Parcelas
    path('CargaParcela/add/', CargaParcela.as_view(), name='CargaParcela'),
    path('EditParcela/edit/<int:pk>/', EditParcela.as_view(), name='EditParcela'),
    path('DeleteParcela/delete/<int:pk>/',
         DeleteParcela.as_view(), name='DeleteParcela'),
    # Empleados
    path('ListaEmpleado/', views.ListaEmpleado.as_view(), name='ListaEmpleado'),
    path('CargaEmployee/add/', CargaEmployee.as_view(), name='CargaEmployee'),
    path('EditEmployee/edit/<int:pk>/',
         EditEmployee.as_view(), name='EditEmployee'),
    path('DeleteEmployee/delete/<int:pk>/',
         DeleteEmployee.as_view(), name='DeleteEmployee'),
    # trabajo prueba
    path('SaleCreateView/add/', SaleCreateView.as_view(), name='SaleCreateView'),

    # Camiones
    path('CargaCamion/add/', CargaCamion.as_view(), name='CargaCamion'),
    path('EditCamion/edit/<int:pk>/', EditCamion.as_view(), name='EditCamion'),
    path('DeleteCamion/delete/<int:pk>/',
         DeleteCamion.as_view(), name='DeleteCamion'),
    # Entregas
    path('CargaEntregas/add/', CargaEntregas.as_view(), name='CargaEntregas'),
    path('EditEntregas/edit/<int:pk>/',
         EditEntregas.as_view(), name='EditEntregas'),
    path('DeleteEntregas/delete/<int:pk>/',
         DeleteEntregas.as_view(), name='DeleteEntregas'),
    # Clientes
    path('CargaCliente/add/', CargaCliente.as_view(), name='CargaCliente'),
    path('EditCliente/edit/<int:pk>/', EditCliente.as_view(), name='EditCliente'),
    path('DeleteCliente/delete/<int:pk>/',
         DeleteCliente.as_view(), name='DeleteCliente'),
    # Proveedores
    path('CargaProveedor/add/', CargaProveedor.as_view(), name='CargaProveedor'),
    path('EditProveedor/edit/<int:pk>/',
         EditProveedor.as_view(), name='EditProveedor'),
    path('DeleteProveedor/delete/<int:pk>/',
         DeleteProveedor.as_view(), name='DeleteProveedor'),
    # Produccion
    path('CargaProduccion/add/', CargaProduccion.as_view(), name='CargaProduccion'),
    path('EditProduccion/edit/<int:pk>/',
         EditProduccion.as_view(), name='EditProduccion'),
    path('DeleteProduccion/delete/<int:pk>/',
         DeleteProduccion.as_view(), name='DeleteProduccion'),
]
