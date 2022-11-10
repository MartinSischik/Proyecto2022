from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect


class LoginFormView(LoginView):
    template_name = 'templates/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('stock')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Iniciar Sesión'
        return contexto
