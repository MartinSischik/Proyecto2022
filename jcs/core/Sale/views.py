from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.forms import TrabajoForm
from core.mixins import ValidatePermissionRequiredMixin
from django.views.generic import CreateView
from django.db import transaction
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
                    #item['value'] = i.name
                    item['text'] = i.nombre
                    data.append(item)
            # elif action == 'add':
            #     with transaction.atomic():
            #         vents = json.loads(request.POST['vents'])
            #         sale = Sale()
            #         sale.date_joined = vents['date_joined']
            #         sale.cli_id = vents['cli']
            #         sale.subtotal = float(vents['subtotal'])
            #         sale.iva = float(vents['iva'])
            #         sale.total = float(vents['total'])
            #         sale.save()
            #         for i in vents['products']:
            #             det = DetSale()
            #             det.sale_id = sale.id
            #             det.prod_id = i['id']
            #             det.cant = int(i['cant'])
            #             det.price = float(i['pvp'])
            #             det.subtotal = float(i['subtotal'])
            #             det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
