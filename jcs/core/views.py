
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
# Create your views here.

def Inicio(request):
    return render(request,'template\empty.html')
#C:\Users\Usuario\Desktop\Programacion\proyecto2022\jcs\template\index.html