from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from crum import get_current_user

# Create your models here.
from auditlog.registry import auditlog


class Type (models.Model):
    name = models.CharField(max_length=150, verbose_name=' Nombres ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Employee (models.Model):
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, verbose_name=' Tipo de empleado ')
    name = models.CharField(max_length=150, verbose_name=' Nombres ')
    ci = models.CharField(max_length=10, unique=True, verbose_name=' Ci ')
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']


class Proveedor (models.Model):
    name = models.CharField(max_length=150, verbose_name=' Names ')
    telefono = models.CharField(
        max_length=150, unique=True, verbose_name=' Telefonos ')
    ruc = models.CharField(max_length=150, unique=True, verbose_name=' Ruc ')
    email = models.CharField(
        max_length=150, unique=True, verbose_name=' email ')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedores'
        ordering = ['id']


class Grano (models.Model):
    nombre = models.CharField(max_length=150, verbose_name=' Nombres ')
    variedad = models.CharField(max_length=10,  verbose_name=' Variedad ')
    Procedencia = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.variedad}'

    class Meta:
        verbose_name = 'Semilla'
        verbose_name_plural = 'Semillas'
        db_table = 'Grano'
        ordering = ['id']


class Unidades (models.Model):
    name = models.CharField(max_length=150, verbose_name=' Nombres ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['id']


class CateQuimico (models.Model):
    nombre = models.CharField(
        max_length=150, verbose_name=' CategoriaQ ', null=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Quimico (models.Model):
    name = models.CharField(
        max_length=150, verbose_name=' Nombre ', unique=True)
    categoria = models.ForeignKey(
        CateQuimico, on_delete=models.CASCADE, null=True)
    ingrediente = models.CharField(
        max_length=255, unique=True, verbose_name=' Descripcion ')
    cantidad = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2)
    unidades = models.ForeignKey(Unidades, on_delete=models.CASCADE, null=True)
    procedencia = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.ingrediente}'

    def toJSON(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJSON()

        item['cantidad'] = format(self.cantidad, '.2f')
        # item['unidades'] = self.unidades.toJSON()
        item['precio'] = format(self.precio, '.2f')
        return item


class Meta:
    verbose_name = 'Quimico'
    verbose_name_plural = 'Quimicos'
    db_table = 'Quimicos'
    ordering = ['id']


class Parcelas (models.Model):
    nombre = models.CharField(max_length=150, verbose_name=' Nombres ')
    ubicacion = models.CharField(
        max_length=150,  verbose_name=' Ubicacion ')
    hectareas = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2)

    gasto = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)

        return item

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
        db_table = 'Parcelas'
        ordering = ['id']


class tipo_trabajo (models.Model):
    name = models.CharField(max_length=150, verbose_name=' Nombres ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Trabajo (models.Model):
    parcela = models.ForeignKey(Parcelas, on_delete=models.CASCADE, null=True)
    tipo = models.ForeignKey(tipo_trabajo, on_delete=models.CASCADE, null=True)
    empleado = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    hectareas = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2)
    descripcion = models.CharField(
        max_length=50,  verbose_name=' descripcion ')
    gasto = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    fecha = models.DateField(default=datetime.now)

    def __str__(self):
        return self.tipo

    def toJSON(self):
        item = model_to_dict(self)
        item['parcela'] = self.parcela.toJSON()
        item['tipo'] = self.tipo.toJSON()
        item['empleado'] = self.tipo.toJSON()
        item['gasto'] = format(self.gasto, '.2f')
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        # item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        db_table = 'Trabajos'
        ordering = ['id']


class Det_Trabajo (models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, null=True)
    quimico = models.ForeignKey(Quimico, on_delete=models.CASCADE, null=True)
    cantidad = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2)
    precio = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.quimico.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['trabajo'])
        # item['quimico'] = self.quimico.toJSON()
        item['precio'] = format(self.precio, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Trabajo Detalle'
        verbose_name_plural = 'Trabajo Detalle'
        db_table = 'Trabajo Detalle'
        ordering = ['id']


class camion (models.Model):
    nombre = models.CharField(max_length=40, verbose_name=' Nombres ')
    chapa = models.CharField(max_length=7, unique=True,
                             verbose_name=' Chapas ')
    cedula = models.CharField(
        max_length=7, unique=True, verbose_name=' Cedula ')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Camion'
        verbose_name_plural = 'Camions'
        db_table = 'Camions'
        ordering = ['id']


class Cliente (models.Model):
    nombre = models.CharField(max_length=150, verbose_name=' Nombres ')
    telefono = models.CharField(
        max_length=150, unique=True, verbose_name=' Telefonos ')
    ruc = models.CharField(max_length=150, unique=True, verbose_name=' Ruc ')
    email = models.CharField(
        max_length=150, unique=True, verbose_name=' email ')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'
        ordering = ['id']


class Entregas (models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    camion_id = models.ForeignKey(camion, on_delete=models.CASCADE, null=True)
    grano_id = models.ForeignKey(Quimico, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.now)

    def __str__(self):
        return self.cliente.nombre

    class Meta:
        verbose_name = 'Entregas'
        verbose_name_plural = 'Entregas'
        db_table = 'Entregas'
        ordering = ['id']


class Produccion (models.Model):
    parcela = models.ForeignKey(Parcelas, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Quimico, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.now)

    def __str__(self):
        return self.parcela

    class Meta:
        verbose_name = 'Produccion'
        verbose_name_plural = 'Producciones'
        db_table = 'Produccion'
        ordering = ['id']


auditlog.register(Proveedor)
auditlog.register(Employee)
auditlog.register(Produccion)
auditlog.register(Entregas)
auditlog.register(Cliente)
auditlog.register(camion)
auditlog.register(Parcelas)
auditlog.register(Quimico)
# auditlog.register(CateQuimico)
