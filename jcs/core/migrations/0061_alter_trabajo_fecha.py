# Generated by Django 3.2.7 on 2023-01-26 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_alter_trabajo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]