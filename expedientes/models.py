from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TipoReclamo(models.Model):
    codigo = models.CharField(max_length=2, null=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Expedientes(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    user_carga = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    observacion = models.CharField(max_length=255)
    tipo_reclamo = models.ForeignKey(TipoReclamo, on_delete=models.PROTECT, null=True)
    tema = models.CharField(max_length=100)
    multitudinario = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']