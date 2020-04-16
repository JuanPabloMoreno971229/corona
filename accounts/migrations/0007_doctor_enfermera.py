# Generated by Django 2.0 on 2020-04-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200416_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('l_name', models.CharField(max_length=200, verbose_name='Apellido')),
                ('n_documento', models.CharField(max_length=200, verbose_name='N° de documento')),
                ('registro', models.CharField(max_length=200, verbose_name='Registro profesional')),
                ('lugar', models.CharField(max_length=200, verbose_name='Empresa donde trabaja')),
                ('especialidad', models.CharField(max_length=200, verbose_name='Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('l_name', models.CharField(max_length=200, verbose_name='Apellido')),
                ('n_documento', models.CharField(max_length=200, verbose_name='N° de documento')),
                ('registro', models.CharField(max_length=200, verbose_name='Registro profesional')),
                ('lugar', models.CharField(max_length=200, verbose_name='Empresa donde trabaja')),
                ('especialidad', models.CharField(max_length=200, verbose_name='Especialidad')),
            ],
        ),
    ]
