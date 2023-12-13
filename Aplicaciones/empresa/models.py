from django.db import models
from django.contrib.auth.models import User

from unemi_empleo import settings
from Aplicaciones.estudiante.constantes import *

class Empresa(User):
    ruc = models.CharField(max_length=13,unique=True, null=True)
    nombre = models.CharField(max_length=50,verbose_name='Empresa',unique=True, null=True)
    direccion = models.CharField(max_length=500, null=True)
    telefono = models.CharField(max_length=20, null=True)
    foto = models.FileField(upload_to='empresas/fotos/', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre)
    

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ('nombre',)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)

        return '{}{}'.format(settings.STATIC_URL, settings.PHOTO_USER_EMPTY)



class Vacante(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    carreraRequerida = models.CharField(max_length=3, choices=CHOICES_CARRERA)
    nivelRequerido = models.CharField(max_length=3, choices=CHOICES_NIVEL_EDUCATIVO)
    ubicacion = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fechaIni = models.DateField()
    fechaFin = models.DateField()
    cupos = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{}".format(self.titulo)
