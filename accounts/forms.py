from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Usuario,Enfermera,Doctor


class Encuesta(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Enfermera
        fields = "__all__"
class NurseForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
