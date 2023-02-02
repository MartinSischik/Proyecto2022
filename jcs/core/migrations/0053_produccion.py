# Generated by Django 4.1 on 2023-01-17 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_parcelas_trabajos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('parcela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.parcelas')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.grano')),
            ],
            options={
                'verbose_name': 'Produccion',
                'verbose_name_plural': 'Producciones',
                'db_table': 'Produccion',
                'ordering': ['id'],
            },
        ),
    ]