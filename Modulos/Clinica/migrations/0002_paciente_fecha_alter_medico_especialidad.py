# Generated by Django 4.2.5 on 2023-10-16 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.CharField(max_length=20),
        ),
    ]