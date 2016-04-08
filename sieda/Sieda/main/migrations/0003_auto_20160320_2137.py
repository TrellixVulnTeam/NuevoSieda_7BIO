# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 03:37
from __future__ import unicode_literals

import datetime
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('main', '0002_auto_20160113_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.IntegerField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Contrasena', models.CharField(max_length=15, verbose_name=b'Contrase\xc3\xb1a')),
                ('Realizado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Abrev_carrera', models.CharField(max_length=10, verbose_name=b'Abreviatura')),
            ],
        ),
        migrations.CreateModel(
            name='Catalago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grupo', models.CharField(max_length=100, null=True)),
                ('Cuatrimestre', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='JefeCarrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Abrev_materia', models.CharField(max_length=10, null=True, verbose_name=b'Abreviatura')),
                ('Carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Carrera')),
                ('Grupos', models.ManyToManyField(to='main.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
                ('Realizado', models.BooleanField(default=False)),
                ('Catalagos', models.ManyToManyField(to='main.Catalago')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('Preguntas', models.ManyToManyField(to='main.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Carrera')),
                ('Grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Grupo')),
                ('Maestro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Maestro')),
            ],
        ),
        migrations.DeleteModel(
            name='alumnos',
        ),
        migrations.DeleteModel(
            name='carreras',
        ),
        migrations.DeleteModel(
            name='configuracion',
        ),
        migrations.DeleteModel(
            name='grupos',
        ),
        migrations.DeleteModel(
            name='materias',
        ),
        migrations.DeleteModel(
            name='servicios',
        ),
        migrations.DeleteModel(
            name='tutores',
        ),
        migrations.AlterModelOptions(
            name='administradores',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='administradores',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='administradores',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='administradores',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='administradores',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='administradores',
            name='nom_user',
        ),
        migrations.RemoveField(
            model_name='administradores',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='administradores',
            name='tipo',
        ),
        migrations.AddField(
            model_name='administradores',
            name='Realizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administradores',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 3, 21, 3, 37, 24, 987000, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administradores',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='username',
            field=models.CharField(default=datetime.datetime(2016, 3, 21, 3, 37, 31, 215000, tzinfo=utc), error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maestro',
            name='Materia',
            field=models.ManyToManyField(to='main.Materia'),
        ),
        migrations.AddField(
            model_name='catalago',
            name='Secciones',
            field=models.ManyToManyField(to='main.Seccion'),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Maestro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Maestro'),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Periodo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Periodo'),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Seccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Seccion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Carrera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Carrera'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Grupo'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='Carrera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Carrera'),
        ),
        migrations.AddField(
            model_name='administradores',
            name='Grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Grupo'),
        ),
    ]
