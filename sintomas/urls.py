from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sintomas, name='sintomas'),
    path('pacientes/lista/<int:pk>', views.PacienteDetailView.as_view(), name='paciente-detail'),
    path('pacientes/lista/', views.PacienteListView.as_view(), name='pacientes'),
    path('encuestas/',views.encuesta,name="encuesta"),
    path('estadisticas/',views.stats,name="stats"),



]
