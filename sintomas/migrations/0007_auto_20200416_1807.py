# Generated by Django 2.0 on 2020-04-16 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sintomas', '0006_auto_20200416_1805'),
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
