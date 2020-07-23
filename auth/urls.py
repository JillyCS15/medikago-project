from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/admin', views.register_admin, name='register-admin'),
    path('register/doctor', views.register_doctor, name='register-doctor'),
    path('register/patient', views.register_patient, name='register-patient'),
    path('logout/', views.logout, name='logout'),
]