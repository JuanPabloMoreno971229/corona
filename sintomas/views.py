from django.shortcuts import render,redirect
from .forms import SintomasForm,Encuesta
from django.views.generic import DetailView
from django.views import generic

from .models import Paciente,Sintomas

# Create your views here.
def sintomas(request):
    if request.method == "POST":
        form = SintomasForm(request.POST)
        if form.is_valid():
            dan = request.user
            print(dan)
            form.save()
            return redirect('chao')

    else:
            form = SintomasForm()
    return render(request,'sintomas/sintomas.html',{'form':form})
a = Sintomas.objects.all()
print(a.query)
p_fiebre = Sintomas.objects.all().filter(fiebre=True)
pa_fiebre = p_fiebre.count()

p_tos = Sintomas.objects.all().filter(tos=True)

pa_tos = p_fiebre.count()

p_moco = Sintomas.objects.all().filter(moco=True)
pa_moco = p_moco.count()

p_congestion =Sintomas.objects.all().filter(congestion=True)
pa_congestion = p_congestion.count()

p_estornudos = Sintomas.objects.all().filter(estornudos=True)
pa_estornudos = p_estornudos.count()

p_d_garganta =Sintomas.objects.all().filter(d_garganta=True)
pa_d_garganta = p_d_garganta.count()

p_d_respirar = Sintomas.objects.all().filter(d_respirar=True)
pa_d_respirar = p_d_respirar.count()

p_flema =Sintomas.objects.all().filter(flema=True)
pa_flema = p_flema.count()

p_vomito = Sintomas.objects.all().filter(vomito=True)
pa_vomito = p_vomito.count()

p_diarrea =Sintomas.objects.all().filter(diarrea=True)
pa_diarrea = p_diarrea.count()

p_cansancio = Sintomas.objects.all().filter(cansancio=True)
pa_cansancio = p_cansancio.count()

p_quebrahueso =Sintomas.objects.all().filter(quebrahueso=True)
pa_quebrahueso = p_quebrahueso.count()

p_x_ray = Sintomas.objects.all().filter(x_ray=True)
pa_x_ray = p_x_ray.count()

print(pa_fiebre)
class PacienteDetailView(generic.DetailView):

    model = Paciente


    def get_context_data(self, **kwargs):
        context = super(PacienteDetailView, self).get_context_data(**kwargs)
        context['fiebre'] = Sintomas.objects.all().filter(fiebre=True)
        #context['tos'] = a[0]

        return context
class PacienteListView(generic.ListView):

    model = Paciente
    order_by = 'f_name'
    paginate_by = 20
    template_name = 'sintomas/sintomas_list.html'
    def get_context_data(self, **kwargs):
        context = super(PacienteListView, self).get_context_data(**kwargs)
        context['pa_fiebre'] = pa_fiebre
        context['pa_tos'] = pa_tos
        context['pa_moco'] = pa_moco
        context['pa_congestion'] = pa_congestion
        context['pa_estornudos'] = pa_estornudos
        context['pa_d_garganta'] = pa_d_garganta
        context['pa_d_respirar'] = pa_d_respirar
        context['pa_flema'] = pa_flema
        context['pa_vomito'] = pa_vomito
        context['pa_diarrea'] = pa_diarrea
        context['pa_cansancio'] = pa_cansancio
        context['pa_quebrahueso'] = pa_quebrahueso
        context['pa_x_ray'] = pa_x_ray

        return context
def encuesta(request):

    if request.method == "POST":
        form = Encuesta(request.POST)
        if form.is_valid():
            dan = request.user
            print(dan)
            form.save()
            return redirect('sintomas')

    else:
            form = Encuesta()
    return render(request,'sintomas/encuesta.html',{'form':form})
def stats(request):
    
    return render(request,'sintomas/stats.html')
