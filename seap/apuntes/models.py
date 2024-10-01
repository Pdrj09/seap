from django.db import models
from django.forms import CharField, IntegerField
from django.contrib.auth.models import User


# Create your models here.


class Asignaturas(models.Model):
    asignatura = models.CharField(max_length=500)
    semestre = models.IntegerField()
    creditos = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['asignatura']),
        ]

class apuntes(models.Model):
    asignatura = models.OneToOneField(Asignaturas, on_delete=models.CASCADE)
    nombre_tema = models.CharField(max_length=1000)
    dir = models.FileField(upload_to='apuntes/documents')
