from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from Aplicaciones.empresa.models import Empresa

from Aplicaciones.estudiante.models import Estudiante

"""
---------------------------------------------------------------------- Logear ESTUDIANTE
"""
class LoginStudentView(LoginView):
    template_name = 'login\login_student.html'
    success_url = 'inicio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio de sesión | Estudiantes'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            username = self.request.POST['username']
            password = self.request.POST['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                exists_student = Estudiante.objects.filter(user_ptr=user).exists()

                if exists_student:
                    login(request, user)
                    return redirect(self.success_url)
                else:
                    form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
                    return self.form_invalid(form)
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
                return self.form_invalid(form)

        return self.form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})




        


"""
---------------------------------------------------------------------- Logear EMPRESA
"""
class LoginCompanyView(LoginView):
    template_name = 'login\login_company.html'
    success_url = 'inicioCompany'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio de sesión | Unemi Empresas'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.get_form()

        if form.is_valid():
            username = self.request.POST['username']
            password = self.request.POST['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                exists_Company = Empresa.objects.filter(user_ptr=user).exists()

                if exists_Company:
                    login(request, user)
                    return redirect(self.success_url)
                else:
                    form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
                    return self.form_invalid(form)
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
                return self.form_invalid(form)

        return self.form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
