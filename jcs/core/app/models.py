from django.db import models

# Create your models here.
class Empleado(models.Model):
    names = models.CharField(max_length=100,verbose_name='Nombres')
    ci = models.CharField(max_length=10,unique=True,verbose_name='CI')
