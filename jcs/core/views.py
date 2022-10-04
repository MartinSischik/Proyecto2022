
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
# Create your views here.

def Inicio(request):
    return render(request,'templates\index.html')

def vacio(request):
    return render(request,'templates\empty.html')

def stock(request):
    return render(request,'templates\Stock.html')