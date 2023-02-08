

from auditlog.models import LogEntry
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request, HttpResponseRedirect
from core.forms import *
from core.mixins import IsSupperusserMixin, ValidatePermissionRequiredMixin
from core.models import *
from core.models import Grano
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from login.views import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def home(request):
    return render(request, 'templates\index.html')


@login_required
# este se puede usar en cualquier Request
def Inicio(request):

    listatabla2 = Grano.objects.all()
    listatabla1 = Produccion.objects.all()
    listatabla3 = CateQuimico.objects.all()
    listatabla4 = Parcelas.objects.all()

    pagina = 'templates\EntregaStock.html'
    return render(request, 'templates\Inicio.html', {"listatabla1": listatabla1, "listatabla2": listatabla2, "listatabla3": listatabla3, "listatabla4": listatabla4, "pagina": pagina})


# Quimico
# @csrf_exempt
class CargaQuimico(CreateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock2')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Stock '
        contexto['accion'] = 'Crear'
        return contexto


class EditQuimico(UpdateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock2')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Stock '
        contexto['accion'] = 'Crear'
        return contexto


class DeleteQuimico(DeleteView):
    model = Quimico
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Agroquimico'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('stock2')
        return contexto


class CatQuimiCreateview(CreateView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nueva Categoria de Stock'
        contexto['accion'] = 'Crear'
        return contexto


class CatQuimiEditview(UpdateView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Categoria de Stock'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteQuimiCate(DeleteView):
    model = CateQuimico
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Categoria'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('inicio')
        return contexto


# Grano
class CargaGrano(CreateView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Stock de Semilla'
        contexto['accion'] = 'Crear'
        return contexto


class EditGrano(UpdateView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Stock de Semilla'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteGrano(DeleteView):
    model = Grano
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Semilla'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('stock')
        return contexto


# Parcela
class CargaParcela(CreateView):
    model = Parcelas
    form_class = ParcelaForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Parcela'
        contexto['accion'] = 'Crear'
        return contexto


class EditParcela(UpdateView):
    model = Parcelas
    form_class = ParcelaForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Parcela'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteParcela(DeleteView):
    model = Parcelas
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Parcela'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('inicio')
        return contexto


@login_required
# Entregas
def Entregas_Stock(request):

    listatabla1 = Grano.objects.all()
    listatabla2 = camion.objects.all()
    listatabla3 = Entregas.objects.all()
    # listatabla4=Parcelas.objects.all()

    pagina = 'templates\EntregaStock.html'
    return render(request, 'templates\EntregaStock.html', {"listatabla1": listatabla1, "listatabla2": listatabla2, "listatabla3": listatabla3, "pagina": pagina})


@login_required
# Entregas
def ListaTrabajo(request):

    listatabla1 = Trabajo.objects.all()

    return render(request, 'templates\ListaTrabajos.html', {"listatabla1": listatabla1})


def ListaDetalleTrabajo(request, id_trabajo):

    listatabla1 = Det_Trabajo.objects.filter(trabajo_id=id_trabajo)

    return render(request, 'templates\Lista_Detalle.html', {"listatabla1": listatabla1})


#
class CargaEntregas(CreateView):
    model = Entregas
    form_class = EntregasForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nueva Entrega'
        contexto['accion'] = 'Crear'

        return contexto

    def post(self, request, *args, **kwargs):
        print(request.POST)
        det = Entregas()
        grano = Quimico.objects.get(id=request.POST.get('grano_id'))
        form = EntregasForm(request.POST)
        form.save()
        grano.cantidad = int(grano.cantidad) - \
            int(request.POST.get('cantidad'))
        grano.save()
        return HttpResponseRedirect(self.success_url)


class EditEntregas(UpdateView):
    model = Entregas
    form_class = EntregasForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        det = Entregas.objects.get(pk=self.get_object().id)
        aux = pk
        aux2 = det.cantidad
        grano2 = Quimico.objects.get(id=det.grano_id_id)
        print(grano2.cantidad)
        suma = grano2.cantidad + aux2
        grano2.cantidad = suma
        grano2.save()
        print(aux2)
        print(suma)
        print('viejo')
        print(grano2.cantidad)

        grano = Quimico.objects.get(id=request.POST.get('grano_id'))
        det.cantidad = int(request.POST.get('cantidad'))
        grano.cantidad = grano.cantidad - det.cantidad
        print(grano2.name)
        print(grano2.cantidad)
        print(grano.name)
        print(grano.cantidad)
        grano.save()
        det.id = aux

        form = EntregasForm(request.POST, instance=det)
        form.save()

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Entregas'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteEntregas(DeleteView):
    model = Entregas
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        det = Entregas.objects.get(pk=self.get_object().id)
        aux = pk
        aux2 = det.cantidad
        grano2 = Quimico.objects.get(id=det.grano_id_id)
        print(grano2.cantidad)
        suma = grano2.cantidad + aux2
        grano2.cantidad = suma
        grano2.save()
        det.delete()

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Estas seguro de eliminar esta entrega?'
        contexto['accion'] = 'Eliminar'
        return contexto

# Camion


class CargaCamion(CreateView):
    model = camion
    form_class = CamionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Camion'
        contexto['accion'] = 'Crear'
        return contexto


class EditCamion(UpdateView):
    model = camion
    form_class = CamionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Camion'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteCamion(DeleteView):
    model = camion
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Camion'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('Entregas_Stock')
        return contexto


# CLiente
class ListaCliente(ListView):
    template_name = 'templates\clientes.html'
    model = Cliente

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Cliente'
        contexto['accion'] = 'Editar'
        contexto['proveedores_contexto'] = Proveedor.objects.all()
        return contexto


class CargaCliente(IsSupperusserMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaCliente')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Cliente'
        contexto['accion'] = 'Crear'
        return contexto


class EditCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaCliente')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Cliente'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteCliente(DeleteView):
    model = Cliente
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('ListaCliente')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Cliente'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('ListaCliente')
        return contexto

# Proveedores


class ListaProveedor(ListView):
    template_name = 'templates\Proveedores.html'
    model = Proveedor

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Listar Proveedores'
        contexto['accion'] = 'Listar'
        return contexto


class CargaProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaProveedor')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Proveedor'
        contexto['accion'] = 'Crear'
        return contexto


class EditProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaProveedor')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Proveedor'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteProveedor(DeleteView):
    model = Proveedor
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('ListaProveedor')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Proveedor'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('ListaProveedor')
        return contexto


@login_required
# este se puede usar en cualquier Request
def stock2(request):

    listatabla1 = Quimico.objects.all()
    listatabla3 = CateQuimico.objects.all()
    listatabla4 = Parcelas.objects.all()

    return render(request, 'templates\Stock2.html', {"listatabla1": listatabla1, "listatabla3": listatabla3, "listatabla4": listatabla4})


@login_required
# este se puede usar en cualquier Request
def Parcela(request):

    # listatabla2=Grano.objects.all()
    # listatabla1=Quimico.objects.all()
    # listatabla3=CateQuimico.objects.all()
    listatabla4 = Parcelas.objects.all()

    # "listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,
    return render(request, 'templates\Parcelas.html', {"listatabla4": listatabla4})


class CargaProduccion(CreateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nueva Produccion'
        contexto['accion'] = 'Crear'
        return contexto

    def post(self, request, *args, **kwargs):
        print(request.POST)
        det = Produccion()
        grano = Quimico.objects.get(id=request.POST.get('producto'))
        form = ProduccionForm(request.POST)
        form.save()
        grano.cantidad = int(grano.cantidad) + \
            int(request.POST.get('cantidad'))
        grano.save()
        return HttpResponseRedirect(self.success_url)


class EditProduccion(UpdateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Produccion'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteProduccion(DeleteView):
    model = Produccion
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        det = Produccion.objects.get(pk=self.get_object().id)
        aux = pk
        aux2 = det.cantidad
        grano2 = Quimico.objects.get(id=det.producto_id)
        print(grano2.cantidad)
        suma = grano2.cantidad - aux2
        grano2.cantidad = suma
        grano2.save()
        det.delete()

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Produccion'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('inicio')
        return contexto


class DeleteProduccionNoStock(DeleteView):
    model = Produccion
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Produccion'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('inicio')
        return contexto


class ListaEmpleado(ListView):
    template_name = 'templates\empleado.html'
    model = Employee

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Empleados'
        return contexto


class CargaEmployee(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaEmpleado')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Nuevo Proveedor'
        contexto['accion'] = 'Crear'
        return contexto


class EditEmployee(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaEmpleado')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Employee'
        contexto['accion'] = 'Editar'
        return contexto


class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('ListaEmpleado')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Employee'
        contexto['accion'] = 'Eliminar'

        return contexto


@login_required
@user_passes_test(lambda u: u.is_superuser)
# este se puede usar en cualquier Request
def auditoria(request):
    listatabla4 = LogEntry.objects.all()
    if request.method == 'POST':
        eliminar = LogEntry.objects.all().delete()
        return render(request, 'templates\ditoria.html', {"listatabla4": listatabla4, "eliminar": eliminar})
    else:
        return render(request, 'templates\ditoria.html', {"listatabla4": listatabla4, })


@login_required
# este se puede usar en cualquier Request
def ErrorUsuario(request):

    Error = 'No cuenta con permisos para esta accion'
    return render(request, 'templates\pages\samples\error-404.html', {"Error": Error})
