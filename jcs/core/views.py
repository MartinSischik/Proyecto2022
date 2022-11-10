

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
from core.forms import CateQuimicoForm, GranoForm, ParcelaForm, QuimicoForm
from core.models import CateQuimico, Parcelas, Quimico, Unidades,Employee,CateQuimico
from core.models import Grano
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Stock de Agroquimico'
        contexto['accion']='Crear'
        return contexto

class DeleteQuimico(DeleteView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Agroquimico'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto

class CargaGrano(CreateView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')
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
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Stock de Semilla'
        contexto['accion']='Editar'
        return contexto

class DeleteGrano(DeleteView):
    model = Grano
    form_class = GranoForm
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Semilla'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto

class CatQuimiCreateview(CreateView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')

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

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Categoria de Agroquimico'
        contexto['accion']='Editar'
        return contexto

class DeleteQuimiCate(DeleteView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Categoria'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto

class CargaParcela(CreateView):
    model = Quimico
    form_class = ParcelaForm
    template_name = 'templates\CargaStock.html'
    success_url = reverse_lazy('stock')
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
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Editar Parcela'
        contexto['accion']='Editar'
        return contexto

class DeleteParcela(DeleteView):
    model = Parcelas
    form_class = ParcelaForm
    template_name = 'templates\eliminar.html'
    success_url = reverse_lazy('stock')
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Eliminar Parcela'
        contexto['accion']='Eliminar'
        contexto['list_url']=reverse_lazy('stock')
        return contexto










