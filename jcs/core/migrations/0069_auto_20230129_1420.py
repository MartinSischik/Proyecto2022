# Generated by Django 3.2.7 on 2023-01-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_det_trabajo_trabajo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='nombre',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='name',
            field=models.CharField(default=4444, max_length=150, verbose_name=' Names '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quimico',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name=' Nombre '),
        ),
    ]
