from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from django.urls import reverse_lazy

from core.forms import TrabajoForm
from core.mixins import ValidatePermissionRequiredMixin
from django.views.generic import CreateView

from core.models import Trabajo


class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Trabajo
    form_class = TrabajoForm
    template_name = 'templates/prueba.html'
    success_url = reverse_lazy('inicio')
    permission_required = 'erp.add_sale'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Trabajo'
        context['entity'] = 'Trabajo'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context