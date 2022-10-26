from django.db import models

# Create your models here.


class Type (models.Model):
    name = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
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
    kilogramos = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Semilla'
        verbose_name_plural = 'Semillas' 
        db_table = 'Grano'
        ordering = ['id']

class Unidades (models.Model):
    name = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades' 
        ordering = ['id']

class CateQuimico (models.Model):
    CategoriaQ = models.CharField ( max_length = 150 , verbose_name = ' CategoriaQ ',default="no_description", null=True)
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias' 
        ordering = ['id']
class Quimico ( models.Model ) :
    Categoria =models.ForeignKey(CateQuimico,on_delete=models.PROTECT,null=True)
    unidades =models.ForeignKey(Unidades,on_delete=models.PROTECT)
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    ingrediente = models.CharField ( max_length = 10 , unique = True , verbose_name = ' Variedad ' )
    cantidad = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    
    def __str__(self):
        return self.unidades

    class Meta:
        verbose_name = 'Quimico'
        verbose_name_plural = 'Quimicos' 
        db_table = 'Quimicos'
        ordering = ['id']