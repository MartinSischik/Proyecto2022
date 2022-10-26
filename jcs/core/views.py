
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
from core.forms import CateQuimicoForm
from core.models import CateQuimico, Quimico, Unidades,Employee
from core.models import Grano
# Create your views here.

def Inicio(request):
    return render(request,'templates\index.html')

def vacio(request):
    return render(request,'templates\empty.html')

def stock(request):
    listatabla3=Employee.objects.all()
    listatabla2=Grano.objects.all()
    listatabla1=Quimico.objects.all()
    
    return render(request,'templates\Stock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2})

def Cargastock(request):

    listatabla1=Quimico.objects.all()
    listatabla2=Unidades.objects.all()
    return render(request,'templates\CargaStock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2})

def CargaGrano(request):

    listatabla1=Grano.objects.all()
    return render(request,'templates\CargaGrano.html',{"listatabla1":listatabla1})

# class CatQuimiCreateview(CreateView):
#     model = CateQuimico
#     form_class = CateQuimicoForm
#     template_name = 'CargaCateQui.html'