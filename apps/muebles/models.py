import uuid
from django.db import models

class Mueble(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  nombre = models.CharField(max_length=50)
  imagen = models.ImageField(upload_to='muebles/')
  descripcion = models.TextField(blank=True, null=True)
  color = models.CharField(max_length=100, blank=True, null=True)
  medidas = models.CharField(max_length=100, blank=True, null=True)
  precio = models.DecimalField(max_digits=12, decimal_places=2)
  
  def __str__(self):
    return self.nombre