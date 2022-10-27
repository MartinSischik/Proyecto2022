# Generated by Django 3.2.7 on 2022-10-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_rename_categoriaq_catequimico_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quimico',
            old_name='Categoria',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='quimico',
            name='ingrediente',
            field=models.CharField(max_length=10, unique=True, verbose_name=' Ingrediente Activo '),
        ),
        migrations.AlterField(
            model_name='quimico',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name=' Nombre '),
        ),
    ]