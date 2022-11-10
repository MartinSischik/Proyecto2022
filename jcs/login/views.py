from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class LoginFormView(LoginView):
    template_name = 'templates/login.html'


    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        contexto['page_title']='Iniciar Sesión'
        return contexto
