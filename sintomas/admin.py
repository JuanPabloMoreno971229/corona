from django.contrib import admin

# Register your models here.
from .models import Sintomas,Paciente

admin.site.register(Sintomas)
admin.site.register(Paciente)
