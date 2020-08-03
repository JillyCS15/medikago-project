from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('patient/', views.patient_home, name='patient-home'),
    path('doctor/', views.doctor_home, name='doctor-home'),
    path('admin/', views.patient_home, name='admin-home'),
]