from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from core.mixins import ValidatePermissionRequiredMixin
from usuario.forms import UserForm
from usuario.models import User
from urllib import request

from django.shortcuts import render
# from core.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponseRedirect


class UserListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = User
    template_name = 'usuario/templates/list.html'
    permission_required = 'usuario.view_user'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = ''  # reverse_lazy('erp:category_create')
        context['list_url'] = ''  # reverse_lazy('user:user_list')
        context['entity'] = 'Usuarios'
        return context


class UserCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/templates/CargaStock.html'
    success_url = reverse_lazy('UserListView')
    permission_required = 'usuario.add_user'

    @method_decorator(csrf_exempt)
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
        context['title'] = 'Creacion de Usuarios'
        context['entity'] = 'Usuarios'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context


class UserUpdateView(ValidatePermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/templates/Cargastock.html'
    success_url = reverse_lazy('UserListView')
    url_redirect = reverse_lazy('ErrorUsuario')
    permission_required = 'usuario.change_user'
    method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Editar Usuario'
        contexto['action'] = 'edit'
        contexto['list_url'] = self.success_url
        return contexto


class UserDeleteView(ValidatePermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'templates/eliminar.html'
    success_url = reverse_lazy('UserListView')
    url_redirect = success_url
    permission_required = 'usuario.delete_user'
    method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['page_title'] = 'Eliminar Usuario'
        contexto['accion'] = 'Eliminar'
        contexto['list_url'] = reverse_lazy('inicio')
        contexto['entity'] = 'Usuario'
        contexto['nombre'] = self.object.username
        return contexto

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_title'] = 'Eliminación de un Usuario'
    #     context['entity'] = 'Usuarios'
    #     context['list_url'] = self.success_url
    #     return context
