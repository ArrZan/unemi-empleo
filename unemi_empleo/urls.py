from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls.static import static

from unemi_empleo import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="/login/student/")),
    path('login/', include('Aplicaciones.login.urls')),
    path('modulos/', include('Aplicaciones.estudiante.urls')),
    path('modulos/Company/', include('Aplicaciones.empresa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)