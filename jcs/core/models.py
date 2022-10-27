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
    variedad = models.CharField ( max_length = 10 ,  verbose_name = ' Variedad ' )
    procedencia = models.CharField ( max_length = 10, default='' , verbose_name = ' Procedencia ',blank=True ,null=True )
    kilogramos = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    precio = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, null=True ,blank=True)
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
    nombre = models.CharField ( max_length = 150 , verbose_name = ' CategoriaQ ', null=True)
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias' 
        ordering = ['id']
class Quimico ( models.Model ) :
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombre ' )
    categoria =models.ForeignKey(CateQuimico,on_delete=models.PROTECT,null=True)
    ingrediente = models.CharField ( max_length = 10 , unique = True , verbose_name = ' Ingrediente Activo ' )
    cantidad = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    unidades =models.ForeignKey(Unidades,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.unidades

    class Meta:
        verbose_name = 'Quimico'
        verbose_name_plural = 'Quimicos' 
        db_table = 'Quimicos'
        ordering = ['id']

class Parcelas ( models.Model ) :
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    ubicacion = models.CharField ( max_length = 150 , unique = True , verbose_name = ' Ubicacion ' )
    hectareas = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    trabajos = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    gasto = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    def __str__(self):
        return self.unidades

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas' 
        db_table = 'Parcelas'
        ordering = ['id']