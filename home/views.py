from django.shortcuts import render, redirect
from django.db import connection


# Create your views here.
def homepage(request):
    return render(request, '')

def patient_home(request):
    return render(request, '')

def doctor_home(request):
    return render(request, '')

def admin_home(request):
    return render(request, '')
