from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import Encuesta,DoctorForm,NurseForm
from django.views.generic import DetailView, ListView
from django.views import generic
from .models import Enfermera,Doctor

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Usuario  ya existe, favor de utilizar otro'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('verificador')
        else:
            return render(request, 'accounts/signup.html', {'error':'Las contrasenas no son iguales'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'El usuario o contrasena que ha ingresado, es incorrecta. ingrese de nuevo los datos'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('chao')
def home(request):
    #documents = Document.objects.all()
    return render(request, 'accounts/home.html')
def chao(request):
    return render(request,'accounts/chao.html')

def doctor_view(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            print("dan")

            try:
                return redirect('/')
            except:
                pass
    else:
            form = DoctorForm()
    return render(request,'accounts/doctor.html',{'form':form})
def enfermera_view(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
            form = NurseForm()
    return render(request,'accounts/nurse.html',{'form':form})
def verificador(request):
    return render(request,'accounts/verificador.html')
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
    return render(request,'accounts/encuesta.html',{'form':form})
class EnfermeraListView(generic.ListView):

    model = Enfermera

class EnfermeraDetailView(generic.DetailView):

    model = Enfermera

class DoctorListView(generic.ListView):

    model = Doctor
class DoctorDetailView(generic.DetailView):

    model = Doctor
# Create your views here.
