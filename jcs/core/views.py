

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request,HttpResponseRedirect
from core.forms import *
from core.mixins import IsSupperusserMixin
from core.models import *
from core.models import Grano
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from login.views import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def home(request):
    return render(request,'templates\index.html')

@login_required
# este se puede usar en cualquier Request
def Inicio(request):
    
    listatabla2=Grano.objects.all()
    listatabla1=Produccion.objects.all()
    listatabla3=CateQuimico.objects.all()
    listatabla4=Parcelas.objects.all()
    
    pagina='templates\EntregaStock.html'
    return render(request,'templates\Inicio.html',{"listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,"listatabla4":listatabla4, "pagina":pagina})


# Quimico
# @csrf_exempt
class CargaQuimico(CreateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\Test.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Proveedor.objects.filter(name__icontains=request.POST['term'])
                for i in prods:
                    item = i.toJSON()
                    #item['value'] = i.name
                    item['text'] = i.name
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Stock de Agroquimico'
        contexto['accion']='Crear'
        return contexto

class EditQuimico(UpdateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')
    
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
    success_url = reverse_lazy('inicio')
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
    success_url = reverse_lazy('inicio')
    
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
    success_url = reverse_lazy('inicio')

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
    success_url = reverse_lazy('inicio')
    
    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Categoria'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('inicio')
        return contexto


# Grano
class CargaGrano(CreateView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

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
    success_url = reverse_lazy('inicio')

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
    success_url = reverse_lazy('inicio')

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
    success_url = reverse_lazy('inicio')

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
    success_url = reverse_lazy('inicio')

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
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('inicio')
        return contexto

@login_required
# Entregas 
def Entregas_Stock(request):
    
        listatabla1=Grano.objects.all()
        listatabla2=camion.objects.all()
        listatabla3=Entregas.objects.all()
        # listatabla4=Parcelas.objects.all()
        
        pagina='templates\EntregaStock.html'
        return render(request,'templates\EntregaStock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,"pagina":pagina})
    



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
        grano2=Grano.objects.get(id=det.grano_id_id)
        print(grano2.stock)
        suma = grano2.stock + aux2
        grano2.stock=suma
        grano2.save()
        print(aux2)
        print(suma)
        print('viejo')
        print(grano2.stock)
        
        grano=Grano.objects.get(id=request.POST.get('grano_id'))
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


        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Entregas'
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

    def post(self, request,pk,*args,**kwargs):
        det = Entregas.objects.get(pk=self.get_object().id)
        aux = pk
        aux2 = det.cantidad
        grano2=Grano.objects.get(id=det.grano_id_id)
        print(grano2.stock)
        suma = grano2.stock + aux2
        grano2.stock=suma
        grano2.save()
        det.delete()

        
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Entregas'
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
        contexto['page_title']='Eliminar Camion'
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
        contexto['page_title']='Editar Cliente'
        contexto['accion']='Editar'
        contexto['proveedores_contexto']=Proveedor.objects.all()
        return contexto

class CargaCliente(IsSupperusserMixin ,CreateView):
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
        contexto['page_title']='Nuevo Cliente'
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
        contexto['page_title']='Editar Cliente'
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
        contexto['page_title']='Eliminar Cliente'
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
        contexto['page_title']='Nuevo Proveedor'
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
        contexto['page_title']='Editar Proveedor'
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
        contexto['page_title']='Eliminar Proveedor'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('ListaProveedor')
        return contexto

@login_required
# este se puede usar en cualquier Request
def stock2(request):
    
    listatabla2=Grano.objects.all()
    listatabla1=Quimico.objects.all()
    listatabla3=CateQuimico.objects.all()
    listatabla4=Parcelas.objects.all()
    
    
    return render(request,'templates\Stock2.html',{"listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,"listatabla4":listatabla4})

@login_required
# este se puede usar en cualquier Request
def Parcela(request):
    
    # listatabla2=Grano.objects.all()
    # listatabla1=Quimico.objects.all()
    # listatabla3=CateQuimico.objects.all()
    listatabla4=Parcelas.objects.all()
    
    # "listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3,
    return render(request,'templates\Parcelas.html',{"listatabla4":listatabla4})

class CargaProduccion(CreateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nueva Produccion'
        contexto['accion']='Crear'
        return contexto
    
    def post(self, request,*args,**kwargs):
        print(request.POST)
        det = Produccion()
        grano=Grano.objects.get(id=request.POST.get('producto'))
        form =ProduccionForm(request.POST)
        form.save()
        grano.stock = int(grano.stock) + int(request.POST.get('cantidad'))
        grano.save()
        return HttpResponseRedirect(self.success_url)

class EditProduccion(UpdateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Produccion'
        contexto['accion']='Editar'
        return contexto

class DeleteProduccion(DeleteView):
    model = Produccion
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,pk,*args,**kwargs):
        det = Produccion.objects.get(pk=self.get_object().id)
        aux = pk
        aux2 = det.cantidad
        grano2=Grano.objects.get(id=det.producto_id)
        print(grano2.stock)
        suma = grano2.stock - aux2
        grano2.stock=suma
        grano2.save()
        det.delete()

        
        return HttpResponseRedirect(self.success_url)
        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Produccion'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('inicio')
        return contexto

class DeleteProduccionNoStock(DeleteView):
    model = Produccion
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

        
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Produccion'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('inicio')
        return contexto

class CargaTrabajo(CreateView):
    model =Trabajo
    form_class = TrabajoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Nuevo Camion'
        contexto['accion']='Crear'
        return contexto

class EditTrabajo(UpdateView):
    model = Trabajo
    form_class = TrabajoForm
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

class DeleteTrabajo(DeleteView):
    model = Trabajo
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('Entregas_Stock')

    @method_decorator(login_required)
    # se necesita el def dipatch para poder verificar si esta iniciada la sesion
    def dispatch(self, request, *args , **kwargs ) :
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Camion'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('Entregas_Stock')
        return contexto