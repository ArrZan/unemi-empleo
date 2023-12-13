from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Aplicaciones.empresa.mixins import isCompanyMixin


"""
---------------------------------------------------------------------- Pantalla de mis modulos (Empresas)
"""
class ModuloCompanyTV(LoginRequiredMixin, isCompanyMixin, TemplateView):
    template_name = "empresa/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modulos"
        context['home'] = "/modulos/Company/"
        return context