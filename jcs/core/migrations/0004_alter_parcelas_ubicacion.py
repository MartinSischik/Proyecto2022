# Generated by Django 3.2.7 on 2023-02-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_names_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelas',
            name='ubicacion',
            field=models.CharField(max_length=150, verbose_name=' Ubicacion '),
        ),
    ]