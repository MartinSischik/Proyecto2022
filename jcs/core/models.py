from django.db import models

# Create your models here.
class Employee ( models.Model ) :
    names = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    ci = models.CharField ( max_length = 10 , unique = True , verbose_name = ' Ci ' )

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados' 
        db_table = 'empleado'
        ordering = ['id']
    