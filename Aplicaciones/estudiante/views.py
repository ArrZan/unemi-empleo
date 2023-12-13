from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Aplicaciones.estudiante.mixins import isStudentMixin


"""
---------------------------------------------------------------------- Pantalla de mis modulos (estudiantes)
"""
class ModuloTV(LoginRequiredMixin, isStudentMixin, TemplateView):
    template_name = "estudiante/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modulos"
        context['home'] = "/modulos/"
        return context