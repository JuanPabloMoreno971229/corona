from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Sintomas


class SintomasForm(forms.ModelForm):
    fiebre = forms.BooleanField()
    tos = forms.BooleanField()
    moco = forms.BooleanField()
    congestion = forms.BooleanField()
    estornudos = forms.BooleanField()
    d_garganta = forms.BooleanField()
    m_garganta = forms.BooleanField()
    d_respirar = forms.BooleanField()
    flema = forms.BooleanField()
    vomito = forms.BooleanField()
    diarrea = forms.BooleanField()
    cansancio = forms.BooleanField()
    quebrahueso = forms.BooleanField()
    x_ray = forms.BooleanField()
    class Meta:
        model = Sintomas
        fields = "__all__"
