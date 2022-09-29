from django.db import models

# Create your models here.


class Type (models.Model):
    names = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos' 
        ordering = ['id']
class Employee ( models.Model ) :
    type =models.ForeignKey(Type,on_delete=models.PROTECT)
    names = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    ci = models.CharField ( max_length = 10 , unique = True , verbose_name = ' Ci ' )
    salary = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados' 
        db_table = 'empleado'
        ordering = ['id']
    
class Grano ( models.Model ) :
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    variedad = models.CharField ( max_length = 10 , unique = True , verbose_name = ' Variedad ' )
    Kilogramos = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    
    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Semilla'
        verbose_name_plural = 'Semillas' 
        db_table = 'Grano'
        ordering = ['id']
        