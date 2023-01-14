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
    

class Proveedor ( models.Model ) :
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    telefono = models.CharField ( max_length = 150 , unique = True , verbose_name = ' Telefonos ' )
    ruc = models.CharField ( max_length = 150 , unique = True , verbose_name = ' Ruc ' )
    email = models.CharField ( max_length = 150 , unique = True , verbose_name = ' email ' )
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores' 
        db_table = 'Proveedores'
        ordering = ['id']
class Grano ( models.Model ) :
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    variedad = models.CharField ( max_length = 10 ,  verbose_name = ' Variedad ' )
    Procedencia =models.ForeignKey(Proveedor,on_delete=models.PROTECT)
    stock = models.IntegerField(default=0)
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
    categoria =models.ForeignKey(CateQuimico,on_delete=models.CASCADE,null=True)
    ingrediente = models.CharField ( max_length = 10 , unique = True , verbose_name = ' Ingrediente Activo ' )
    cantidad = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    unidades =models.ForeignKey(Unidades,on_delete=models.CASCADE,null=True)
    procedencia =models.ForeignKey(Proveedor,on_delete=models.PROTECT)
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
    trabajos = models.IntegerField(default=0)
    gasto = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas' 
        db_table = 'Parcelas'
        ordering = ['id']

class tipo_trabajo (models.Model):
    name = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos' 
        ordering = ['id']

class Trabajo ( models.Model ) :
    nombre =models.ForeignKey(Parcelas,on_delete=models.PROTECT,null=True)
    tipo =models.ForeignKey(tipo_trabajo,on_delete=models.PROTECT,null=True)
    hectareas = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    descripcion = models.CharField ( max_length = 50 , unique = True , verbose_name = ' descripcion ' )
    gasto = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos' 
        db_table = 'Trabajos'
        ordering = ['id']


class Trabajo_stock ( models.Model ) :
    trabajo_id =models.ForeignKey(Trabajo,on_delete=models.PROTECT,null=True)
    quimico_id =models.ForeignKey(Quimico,on_delete=models.PROTECT,null=True)
    cantidad = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    gasto = models.DecimalField(default=0.00, max_digits=12,decimal_places=2)
    def __str__(self):
        return self.trabajo_id

    class Meta:
        verbose_name = 'Trabajo Stock'
        verbose_name_plural = 'Trabajo Stock' 
        db_table = 'Trabajo Stock'
        ordering = ['id']

class camion ( models.Model ) :
    nombre = models.CharField ( max_length = 40 , verbose_name = ' Nombres ' )
    chapa = models.CharField ( max_length = 7 , unique = True , verbose_name = ' Chapas ' )
    cedula = models.CharField ( max_length = 7 , unique = True , verbose_name = ' Cedula ' )
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Camion'
        verbose_name_plural = 'Camions' 
        db_table = 'Camions'
        ordering = ['id']
    
class Cliente ( models.Model ) :
    nombre = models.CharField ( max_length = 150 , verbose_name = ' Nombres ' )
    telefono = models.CharField ( max_length = 150 , unique = True , verbose_name = ' Telefonos ' )
    ruc = models.CharField ( max_length = 150 , unique = True , verbose_name = ' Ruc ' )
    email = models.CharField ( max_length = 150 , unique = True , verbose_name = ' email ' )
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes' 
        db_table = 'Clientes'
        ordering = ['id']    



class Entregas ( models.Model ) :
    id=models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
    camion_id =models.ForeignKey(camion,on_delete=models.CASCADE,null=True)
    grano_id =models.ForeignKey(Grano,on_delete=models.CASCADE,null=True)
    cantidad = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.cliente.nombre

    class Meta:
        verbose_name = 'Entregas'
        verbose_name_plural = 'Entregas' 
        db_table = 'Entregas'
        ordering = ['id']


    
