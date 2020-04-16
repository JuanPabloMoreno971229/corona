from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('login/',views.login,name="login"),
    path('encuesta/',views.encuesta,name="encuesta"),
    path('doctor/',views.doctor_view,name="doctor"),
    path('enfermera/',views.enfermera_view,name="enfermera"),

    path('verificador/',views.verificador,name="verificador"),

    path('exit/',views.chao,name="chao"),
]
