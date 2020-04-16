from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse #generate urls from url patterns

from django.contrib.auth.models import User



class Sintomas(models.Model):
    #paciente = models.ForeignKey(,on_delete=models.SET_NULL,null=True)
    paciente = models.ForeignKey('Paciente', on_delete=models.SET_NULL, null=True)
    #paciente = models.OneToOneField('Paciente',on_delete=models.CASCADE)
    fiebre = models.BooleanField(default=False,verbose_name="¿Tiene fiebre?")
    tos = models.BooleanField(default=False,verbose_name="¿Tiene tos?")
    moco = models.BooleanField(default=False,verbose_name="¿Tiene moco?")
    congestion = models.BooleanField(default=False,verbose_name="¿Tiene congestión nasal?")
    estornudos = models.BooleanField(default=False,verbose_name="¿Tiene estornudos?")
    d_garganta = models.BooleanField(default=False,verbose_name="¿Tiene dolor de garganta?")
    m_garganta = models.BooleanField(default=False,verbose_name="¿Tiene malestar de garganta?")
    d_respirar = models.BooleanField(default=False,verbose_name="¿Tiene dificultad para respirar?")
    flema = models.BooleanField(default=False,verbose_name="¿Tiene flema?")
    vomito = models.BooleanField(default=False,verbose_name="¿Tiene vómito?")
    diarrea = models.BooleanField(default=False,verbose_name="¿Tiene diarrea?")
    cansancio = models.BooleanField(default=False,verbose_name="¿Tiene cansancio?")
    quebrahueso = models.BooleanField(default=False,verbose_name="¿Tiene quebrahueso?")
    x_ray = models.BooleanField(default=False,verbose_name="¿Tiene mancha en el pulmón?")
    def get_absolute_url(self):

## THIS RETURNS AN URL FOR A CLIENT INSTANCE####
        return reverse('paciente-detail', args=[str(self.id)])
# Create your models here.
class Paciente(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    ## Nombre y apellidos
    f_name = models.CharField(max_length=200,verbose_name="Nombres")
    l_name = models.CharField(max_length=200,verbose_name="Apellidos")
    n_documento = models.CharField(max_length=14,verbose_name="Numero de documento")
    address = models.CharField(max_length=200,verbose_name="Direccion")
    ciudades =(
    ("Aguachica","Aguachica"),
    ("Apartadó", "Apartadó"),
    ("Arauca", "Arauca"),
    ("Armenia", "Armenia"),
    ("Barrancabermeja", "Barrancabermeja"),
    ("Barranquilla", "Barranquilla"),
    ("Bello", "Bello"),
    ("Bogotá", "Bogotá"),
    ("Bucaramanga", "Bucaramanga"),
    ("Buenaventura", "Buenaventura"),
    ("Buga", "Buga"),
    ("Cali", "Cali"),
    ("Cartago", "Cartago"),
    ("Cartagena", "Cartagena"),
    ("Caucasia", "Caucasia"),
    ("Cereté", "Cereté"),
    ("Chia", "Chia"),
    ("Ciénaga", "Ciénaga"),
    ("Cúcuta", "Cúcuta"),
    ("Dosquebradas", "Dosquebradas"),
    ("Duitama", "Duitama"),
    ("Envigado", "Envigado"),
    ("Facatativá", "Facatativá"),
    ("Florencia", "Florencia"),
    ("Floridablanca", "Floridablanca"),
    ("Fusagasugá", "Fusagasugá"),
    ("Girardot", "Girardot"),
    ("Girón", "Girón"),
    ("Ibagué", "Ibagué"),
    ("Ipiales", "Ipiales"),
    ("Itagüí", "Itagüí"),
    ("Jamundí", "Jamundí"),
    ("Lorica", "Lorica"),
    ("Los Patios", "Los Patios"),
    ("Magangué", "Magangué"),
    ("Maicao", "Maicao"),
    ("Malambo", "Malambo"),
    ("Medellín", "Medellín"),
    ("Manizales", "Manizales"),
    ("Melgar", "Melgar"),
    ("Montería", "Montería"),
    ("Neiva", "Neiva"),
    ("Ocaña", "Ocaña"),
    ("Paipa", "Paipa"),
    ("Palmira", "Palmira"),
    ("Pamplona", "Pamplona"),
    ("Pasto", "Pasto"),
    ("Pereira", "Pereira"),
    ("Piedecuesta", "Piedecuesta"),
    ("Pitalito", "Pitalito"),
    ("Popayán", "Popayán"),
    ("Quibdó", "Quibdó"),
    ("Riohacha", "Riohacha"),
    ("Rionegro", "Rionegro"),
    ("Sabanalarga", "Sabanalarga"),
    ("Sahagún", "Sahagún"),
    ("San Andrés Isla", "San Andrés Isla"),
    ("Santa Marta", "Santa Marta"),
    ("Sincelejo", "Sincelejo"),
    ("Soacha", "Soacha"),
    ("Sogamoso", "Sogamoso"),
    ("Soledad", "Soledad"),
    ("Tibú", "Tibú"),
    ("Tuluá", "Tuluá"),
    ("Tumaco", "Tumaco"),
    ("Tunja", "Tunja"),
    ("Turbo", "Turbo"),
    ("Valledupar", "Valledupar"),
    ("Villa de leyva", "Villa de leyva"),
    ("Villa del Rosario", "Villa del Rosario"),
    ("Villavicencio", "Villavicencio"),
    ("Yopal", "Yopal"),
    ("Yumbo", "Yumbo"),
    ("Zipaquirá", "Zipaquirá")
    )
    city = models.CharField(max_length=200,verbose_name="Ciudades",choices=ciudades,default="Zipaquirá")
    departamentos =(
    ("Amazonas", "Amazonas"),
    ("Antioquia", "Antioquia"),
    ("Arauca", "Arauca"),
    ("Atlántico", "Atlántico"),
    ("Bolívar", "Bolívar"),
    ("Boyacá", "Boyacá"),
    ("Bogotá DC", "Bogotá DC"),
    ("Caldas", "Caldas"),
    ("Caquetá", "Caquetá"),
    ("Casanare", "Casanare"),
    ("Cauca", "Cauca"),
    ("Cesar", "Cesar"),
    ("Chocó", "Chocó"),
    ("Córdoba", "Córdoba"),
    ("Cundinamarca", "Cundinamarca"),
    ("Guainía", "Guainía"),
    ("Guaviare", "Guaviare"),
    ("Huila", "Huila"),
    ("La Guajira","La Guajira"),
    ("Magdalena", "Magdalena "),
    ("Meta", "Meta"),
    ("Nariño", "Nariño"),
    ("Norte de Santander", "Norte de Santander"),
    ("Putumayo", "Putumayo"),
    ("Quindío", "Quindío"),
    ("Risaralda", "Risaralda"),
    ("San Andrés y Providencia", "San Andrés y Providencia"),
    ("Santander", "Santander"),
    ("Sucre", "Sucre"),
    ("Tolima", "Tolima"),
    ("Valle del Cauca", "Valle del Cauca"),
    ("Vaupés", "Vaupés"),
    ("Vichada", "Vichada"),

    )
    departamento = models.CharField(max_length=200,choices=departamentos,default="Vichada")
    pais = CountryField()
    phone = models.CharField(max_length=200,verbose_name="Numero telefonico")
    skype = models.CharField(max_length=200,verbose_name="Skype ID")
    generos = (
        ("Mujer","Mujer"),
        ("Hombre","Hombre"),
        ("Otro","Otro"),
    )
    gender = models.CharField(max_length=200,choices=generos,default="Hombre",verbose_name="Genero") ##CHOICE
    age = models.IntegerField(verbose_name="Edad")
    weight = models.IntegerField(verbose_name="Peso en Kilogramos")
    height = models.IntegerField(verbose_name="Estatura en Centimetros")
    email = models.EmailField(verbose_name="Correo Electronico")
    def get_absolute_url(self):

## THIS RETURNS AN URL FOR A CLIENT INSTANCE####
        return reverse('paciente-detail', args=[str(self.id)])
    def __str__(self):
        #### THE NAME IS GOING TO BE DISPLAYED IN THE ADMIN PANNEL ########
        return '{0}'.format(self.f_name)
