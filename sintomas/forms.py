from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Sintomas,Paciente

class Encuesta(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"

class SintomasForm(forms.ModelForm):

    fiebre = forms.BooleanField(required=False,label = '¿Tiene fiebre?')
    tos = forms.BooleanField(required=False)
    moco = forms.BooleanField(required=False)
    congestion = forms.BooleanField(required=False)
    estornudos = forms.BooleanField(required=False)
    d_garganta = forms.BooleanField(required=False)
    m_garganta = forms.BooleanField(required=False)
    d_respirar = forms.BooleanField(required=False)
    flema = forms.BooleanField(required=False)
    vomito = forms.BooleanField(required=False)
    diarrea = forms.BooleanField(required=False)
    cansancio = forms.BooleanField(required=False)
    quebrahueso = forms.BooleanField(required=False)
    x_ray = forms.BooleanField(required=False)
    class Meta:
        model = Sintomas

        fields = "__all__"
        labels = {
            'fiebre' : 'Dani fiebre',
        }
        #widgets = {'paciente':forms.HiddenInput()}
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(SintomasForm,self).__init__(*args,**kwargs)
