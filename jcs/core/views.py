
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import request
# Create your views here.

def Inicio(request):
    return render(request,'template/index.html')
