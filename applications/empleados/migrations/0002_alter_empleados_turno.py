# Generated by Django 5.0.1 on 2024-01-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='turno',
            field=models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], max_length=1, verbose_name='Turno'),
        ),
    ]
