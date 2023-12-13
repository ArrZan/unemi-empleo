from django.urls import path
from .views import ModuloTV

urlpatterns = [
    # modulos/inicio
    path('', ModuloTV.as_view(), name='inicio'),
]

