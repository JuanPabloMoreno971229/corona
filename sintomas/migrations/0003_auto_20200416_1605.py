# Generated by Django 2.0 on 2020-04-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sintomas', '0002_auto_20200416_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sintomas',
            name='paciente',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='Sintomas',
        ),
    ]
