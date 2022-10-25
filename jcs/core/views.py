
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
<<<<<<< HEAD
from core.models import Quimico, Unidades
from core.models import Grano
=======
from core.models import Quimico
from core.models import Grano
from core.models import Employee
>>>>>>> 4a23da493ec97a101c03d71cfde680badfa39898
# Create your views here.

def Inicio(request):
    return render(request,'templates\index.html')

def vacio(request):
    return render(request,'templates\empty.html')

def stock(request):
    listatabla3=Employee.objects.all()
    listatabla2=Grano.objects.all()
    listatabla1=Quimico.objects.all()
<<<<<<< HEAD
    listatabla2=Grano.objects.all()
    return render(request,'templates\Stock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2})

def Cargastock(request):

    listatabla1=Quimico.objects.all()
    listatabla2=Unidades.objects.all()
    return render(request,'templates\CargaStock.html',{"listatabla1":listatabla1,"listatabla2":listatabla2})

def CargaGrano(request):

    listatabla1=Grano.objects.all()
    return render(request,'templates\CargaGrano.html',{"listatabla1":listatabla1})
=======
    return render(request,'templates\Stock.html',{"quimico":listatabla1,"granos":listatabla2})
>>>>>>> 4a23da493ec97a101c03d71cfde680badfa39898
