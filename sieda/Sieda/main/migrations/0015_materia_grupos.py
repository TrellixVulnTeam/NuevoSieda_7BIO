# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_calificaciones_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='Grupos',
            field=models.ManyToManyField(to='main.Grupo'),
        ),
    ]
