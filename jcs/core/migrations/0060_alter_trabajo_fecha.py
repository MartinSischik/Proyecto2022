# Generated by Django 3.2.7 on 2023-01-25 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_auto_20230125_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='fecha',
            field=models.DateField(),
        ),
    ]