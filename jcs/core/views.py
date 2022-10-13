
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
from core.models import Quimico
from core.models import Grano
from core.models import Employee
# Create your views here.

def Inicio(request):
    return render(request,'templates\index.html')

def vacio(request):
    return render(request,'templates\empty.html')

def stock(request):
    listatabla3=Employee.objects.all()
    listatabla2=Grano.objects.all()
    listatabla1=Quimico.objects.all()
    return render(request,'templates\Stock.html',{"quimico":listatabla1,"granos":listatabla2})