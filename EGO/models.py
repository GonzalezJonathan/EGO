from django.db import models

# Create your models here.
class Auto(models.Model):
  anio = models.IntegerField()
  modelo = models.CharField(max_length=255)
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  tipo = models.CharField(max_length=255)
  caracteristica = models.CharField(max_length=255)
  descripcion = models.TextField()