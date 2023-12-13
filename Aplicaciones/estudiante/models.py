from unemi_empleo import settings
from django.db import models
from django.contrib.auth.models import User


from Aplicaciones.empresa.models import Empresa
from Aplicaciones.estudiante.constantes import *

class Estudiante(User):
    nombre = models.CharField(max_length=50, null=True)
    apellidoPat = models.CharField("Apellido paterno", max_length=50, null=True)
    apellidoMat = models.CharField("Apellido materno", max_length=50, null=True)
    cedula = models.CharField(max_length=10, null=True)
    carrera = models.CharField(max_length=3, choices=CHOICES_CARRERA, null=True)
    nivelEducativo = models.CharField(max_length=3, choices=CHOICES_NIVEL_EDUCATIVO, null=True) 
    telefono = models.CharField(max_length=50, blank=True, null=True)
    foto = models.FileField(upload_to='estudiantes/fotos/', blank=True, null=True)


    def __str__(self):
        return '{} - {}'.format(self.cedula, self.apellidoPat)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ('apellidoPat',)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)

        return '{}{}'.format(settings.STATIC_URL, settings.PHOTO_USER_EMPTY)
        
    

class Postulaciones(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_postulacion = models.DateField()
    estado = models.CharField(max_length=3, choices=CHOICES_ESTADO)

    def __str__(self):
        return '{} - {}'.format(self.estudiante, self.empresa)
    


class Notificaciones(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    tipo = models.CharField(max_length=3, choices=CHOICES_NOTIFICACION)
    fecha = models.DateTimeField(auto_now_add=True)
    prioridad = models.CharField(max_length=1, choices=CHOICES_PRIORIDAD)
    visto = models.BooleanField(default=False) # False: no visto / True: visto

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.estudiante} - {self.empresa}'

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ('-fecha',)