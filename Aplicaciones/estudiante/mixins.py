from django.shortcuts import redirect
from django.contrib import messages

from Aplicaciones.estudiante.models import Estudiante

class isStudentMixin(object):
    def dispatch(self, request, *args, **kwargs):
        is_student = Estudiante.objects.filter(user_ptr=request.user).exists()
        if is_student:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('inicioCompany')