
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
from core.models import Quimico
# Create your views here.

def Inicio(request):
    return render(request,'templates\index.html')

def vacio(request):
    return render(request,'templates\empty.html')

def stock(request):

    listatabla1=Quimico.objects.all()
    return render(request,'templates\Stock.html',{"cod_producto":request.session.get("id"),"listatabla1":listatabla1})