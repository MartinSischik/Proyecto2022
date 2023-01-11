

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request,HttpResponseRedirect
from core.forms import *
from core.models import *
from core.models import Grano
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from login.views import *

# Create your views here.

def Inicio(request):
    return render(request,'templates\login.html')

def home(request):
    return render(request,'templates\home.html')

@login_required
# este se puede usar en cualquier Request
def stock(request):
    
    listatabla2=Grano.objects.all()
    listatabla1=Quimico.objects.all()
    listatabla3=CateQuimico.objects.all()
    listatabla4=Parcelas.objects.all()
    
    pagina='templates\stock1.html'
    return render(request,'templates\Stock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,"listatabla4":listatabla4, "pagina":pagina})


# Quimico
class CargaQuimico(CreateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Stock de Agroquimico'
        contexto['accion']='Crear'
        return contexto

class EditQuimico(UpdateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Stock de Agroquimico'
        contexto['accion']='Crear'
        return contexto

class DeleteQuimico(DeleteView):
    model = Quimico
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Agroquimico'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto

class CatQuimiCreateview(CreateView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nueva Categoria de Agroquimico'
        contexto['accion']='Crear'
        return contexto

class CatQuimiEditview(UpdateView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Categoria de Agroquimico'
        contexto['accion']='Editar'
        return contexto

class DeleteQuimiCate(DeleteView):
    model = CateQuimico
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Categoria'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto


# Grano
class CargaGrano(CreateView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Stock de Semilla'
        contexto['accion']='Crear'
        return contexto

class EditGrano(UpdateView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Stock de Semilla'
        contexto['accion']='Editar'
        return contexto

class DeleteGrano(DeleteView):
    model = Grano
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Semilla'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto


# Parcela
class CargaParcela(CreateView):
    model = Parcelas
    form_class = ParcelaForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Parcela'
        contexto['accion']='Crear'
        return contexto

class EditParcela(UpdateView):
    model = Parcelas
    form_class = ParcelaForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Parcela'
        contexto['accion']='Editar'
        return contexto

class DeleteParcela(DeleteView):
    model = Parcelas
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto


# Entregas 
def Entregas_Stock(request):
    
        listatabla1=Grano.objects.all()
        listatabla2=camion.objects.all()
        listatabla3=Entregas.objects.all()
        # listatabla4=Parcelas.objects.all()
        
        pagina='templates\stock1.html'
        return render(request,'templates\stock1.html',{"listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,"pagina":pagina})
    



# 
class CargaEntregas(CreateView):
    model = Entregas
    form_class = EntregasForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     det = Entregas()
    #     det.grano_id.stock -= det.cantidad
    #     det.grano_id.save
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nueva Entrega'
        contexto['accion']='Crear'
        
        return contexto

    def post(self, request,*args,**kwargs):
        print(request.POST)
        det = Entregas()
        grano=Grano.objects.get(id=request.POST.get('grano_id'))
        form =EntregasForm(request.POST)
        form.save()
        grano.stock = int(grano.stock) - int(request.POST.get('cantidad'))
        grano.save()
        return HttpResponseRedirect(self.success_url)
        
class EditEntregas(UpdateView):
    model = Entregas
    form_class = EntregasForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')
    
    

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self, request,pk,*args,**kwargs):
        det = Entregas.objects.get(pk=self.get_object().id)
        aux = pk
        aux2 = det.cantidad
        grano2=Grano.objects.get(nombre=det.grano_id)
        print(grano2.stock)
        suma = grano2.stock + aux2
        grano2.stock=suma
        grano2.save()
        print(aux2)
        print(suma)
        print('viejo')
        print(grano2.stock)
        
        grano=Grano.objects.get(id=request.POST.get('grano_id'))
        #grano.stock += det.cantidad
        det.cantidad=int(request.POST.get('cantidad'))
        grano.stock =grano.stock- det.cantidad
        print(grano2.nombre)
        print(grano2.stock)
        print(grano.nombre)
        print(grano.stock)
        grano.save()
        det.id=aux

        form =EntregasForm(request.POST, instance=det)
        form.save()
        
        return HttpResponseRedirect(self.success_url)

    # def post(self, request,*args,**kwargs):

    #     print(request.POST)
    #     # det = self.get_object
    #     # grano=Grano.objects.get(id=request.POST.get('grano_id'))
    #     # form =EntregasForm(request.POST)
    #     # form.save()
    #     # grano.stock = int(grano.stock) - int(request.POST.get('cantidad'))
    #     # grano.save()
    #     # return HttpResponseRedirect(self.success_url)
    # Entregas.objects.get(pk)
    #     det = Entregas.objects.get(pk=self.get_object().id)
    #     print(det.cantidad)
    #     grano=Grano.objects.get(id=request.POST.get('grano_id'))
    #     grano.stock += det.cantidad
    #     det.cantidad=int(request.POST.get('cantidad'))
    #     grano.stock -= det.cantidad
    #     grano.save()
    #     return HttpResponseRedirect(self.success_url)
        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Parcela'
        contexto['accion']='Editar'
        return contexto

class DeleteEntregas(DeleteView):
    model = Entregas
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        return contexto

# Camion
class CargaCamion(CreateView):
    model = camion
    form_class = CamionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request,*args,**kwargs):
    #     print(request.POST)
    #     form =CamionForm(request.POST)
            # form.save()
        
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object= None
    #     context=self.get_context_data(**kwargs)
    #     context['form']=form
    #     return render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Camion'
        contexto['accion']='Crear'
        return contexto

class EditCamion(UpdateView):
    model = camion
    form_class = CamionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Camion'
        contexto['accion']='Editar'
        return contexto

class DeleteCamion(DeleteView):
    model = camion
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('Entregas_Stock')
        return contexto
    



# CLiente
class ListaCliente(ListView):
    template_name = 'templates\clientes.html'
    model = Cliente
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Parcela'
        contexto['accion']='Editar'
        contexto['proveedores_contexto']=Proveedor.objects.all()
        return contexto

class CargaCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaCliente')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Parcela'
        contexto['accion']='Crear'
        return contexto

class EditCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaCliente')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Parcela'
        contexto['accion']='Editar'
        return contexto

class DeleteCliente(DeleteView):
    model = Cliente
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('ListaCliente')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('ListaCliente')
        return contexto

# Proveedores
class ListaProveedor(ListView):
    template_name = 'templates\Proveedores.html'
    model = Proveedor
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Listar Proveedores'
        contexto['accion']='Listar'
        return contexto
class CargaProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaProveedor')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Parcela'
        contexto['accion']='Crear'
        return contexto

class EditProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('ListaProveedor')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Parcela'
        contexto['accion']='Editar'
        return contexto

class DeleteProveedor(DeleteView):
    model = Proveedor
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('ListaProveedor')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('ListaProveedor')
        return contexto

