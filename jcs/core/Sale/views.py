# from gettext import translation
from django.db import transaction

import json
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.forms import TrabajoForm
from core.mixins import ValidatePermissionRequiredMixin
from django.views.generic import CreateView
from core.models import *


# class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
#     model = Trabajo
#     form_class = TrabajoForm
#     template_name = 'templates/Trabajo.html'
#     success_url = reverse_lazy('inicio')
#     url_redirect = success_url
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'search_products':
#                 data=[]
#                 prods= Quimico.objects.filter(nombre__icontains=request.POST['term'])
#                 for i in prods:
#                     item=i.toJSON()
#                     item['text']=i.nombre
#                     data.append(item)
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data,safe=False)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creación de un Trabajo'
#         context['entity'] = 'Trabajo'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context

class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Trabajo
    form_class = TrabajoForm
    template_name = 'templates/Trabajo.html'
    success_url = reverse_lazy('inicio')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Quimico.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            elif action == 'add':
                vents=request.POST['vents']
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    # print(vents)
                    sale = Trabajo()
                    sale.fecha = vents['fecha']
                    sale.parcela_id = vents['parcela']
                    sale.gasto = float(vents['gasto'])
                    sale.hectareas = float(vents['hectareas'])
                    sale.tipo_id = vents['tipo']
                    sale.descripcion = vents['descripcion']

                    sale.save()
                    for i in vents['products']:
                        det = Det_Trabajo()
                        det.trabajo_id = sale.id
                        det.quimico_id =i['id']
                        det.cantidad = int(i['cantidad'])
                        det.precio = float(i['precio'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un trabajo'
        context['entity'] = 'Ventas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        return context