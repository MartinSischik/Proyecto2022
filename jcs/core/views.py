
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
from core.forms import CateQuimicoForm, QuimicoForm
from core.models import CateQuimico, Quimico, Unidades,Employee,CateQuimico
from core.models import Grano
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

def Inicio(request):
    return render(request,'templates\index.html')

def home(request):
    return render(request,'templates\home.html')

def stock(request):
    listatabla3=CateQuimico.objects.all()
    listatabla2=Grano.objects.all()
    listatabla1=Quimico.objects.all()
    pagina='templates\stock1.html'
    return render(request,'templates\Stock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2,"listatabla3":listatabla3, "pagina":pagina})

class Cargastock(CreateView):
    model = Quimico
    form_class = QuimicoForm
    template_name = 'templates\CargaQuimico.html'
    success_url = reverse_lazy('stock')

def CargaGrano(request):

    listatabla1=Grano.objects.all()
    return render(request,'templates\CargaGrano.html',{"listatabla1":listatabla1})

class CatQuimiCreateview(CreateView):
    model = CateQuimico
    form_class = CateQuimicoForm
    template_name = 'templates\CargaCateQui.html'
    success_url = reverse_lazy('stock')