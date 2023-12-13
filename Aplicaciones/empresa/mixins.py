from django.shortcuts import redirect
from django.contrib import messages

from Aplicaciones.estudiante.models import Empresa

class isCompanyMixin(object):
    def dispatch(self, request, *args, **kwargs):
        is_Company = Empresa.objects.filter(user_ptr=request.user).exists()
        if is_Company:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('inicio')