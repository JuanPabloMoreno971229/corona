from django.contrib import admin

# Register your models here.
from .models import Usuario,Doctor,Enfermera

admin.site.register(Usuario)
admin.site.register(Doctor)
admin.site.register(Enfermera)
