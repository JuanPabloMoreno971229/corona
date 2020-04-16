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
    path('enfermera/lista/<int:pk>', views.EnfermeraDetailView.as_view(), name='enfermera-detail'),
    path('enfermera/lista/', views.EnfermeraListView.as_view(), name='enfermera_l'),
    path('doctor/lista/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/lista/', views.DoctorListView.as_view(), name='doctor_l'),
    path('exit/',views.chao,name="chao"),
]
