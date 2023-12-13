from django.urls import path
from .views import ModuloCompanyTV

urlpatterns = [
    # modulos/inicio
    path('', ModuloCompanyTV.as_view(), name='inicioCompany'),
]

