from django.db import models

# Create your models here.
class Sintomas(models.Model):
    fiebre = models.BooleanField()
    tos = models.BooleanField()
    moco = models.BooleanField()
    congestion = models.BooleanField()
    estornudos = models.BooleanField()
    d_garganta = models.BooleanField()
    m_garganta = models.BooleanField()
    d_respirar = models.BooleanField()
    flema = models.BooleanField()
    vomito = models.BooleanField()
    diarrea = models.BooleanField()
    cansancio = models.BooleanField()
    quebrahueso = models.BooleanField()
    x_ray = models.BooleanField()
