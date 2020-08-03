from django.shortcuts import render, redirect
from .forms import Login, AdminRegistration, DoctorRegistration, PatientRegistration
from django.contrib import messages
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

import random

# Create your views here.
def login(request):
    if "role" in request.session:
        if request.session["role"] == 'admin':
            return redirect('homepage:homepage-admin')
        elif request.session["role"] == 'doctor':
            return redirect('homepage:homepage-doctor')
        else:
            return redirect('homepage:homepage-patient')
    else:
        context = {
            'login_forms' : Login
        }
        if request.method == 'GET':
            login_forms = Login()
            context['login_forms'] =  login_forms
            return render(request, 'login.html', context)
        else:
            received_form = Login(request.POST)
            if received_form.is_valid():
                username = received_form.cleaned_data.get('username')
                password = received_form.cleaned_data.get('password')
                with connection.cursor() as c:
                    c.execute('SELECT * FROM pengguna WHERE username = %s AND password = %s', [username, password])
                    user = c.fetchall()

                if list(user):
                    with connection.cursor() as c:
                        c.execute('SELECT * FROM administrator WHERE username = %s', [username])
                        user_is_admin = c.fetchall()
                        c.execute('SELECT * FROM dokter WHERE username = %s', [username])
                        user_is_dokter = c.fetchall()

                    request.session["username"] = username
                    if list(user_is_admin):
                        request.session["role"] = "admin"
                        messages.info(request, 'Login successful as an admin!')
                        return redirect('homepage:homepage-admin')
                    elif list(user_is_dokter):
                        request.session["role"] = "doctor"
                        messages.info(request, 'Login successful as a doctor')
                        return redirect('homepage:homepage-dokter')
                    else:
                        request.session["role"] = "patient"
                        messages.info(request, 'Login successful as a patient')
                        return redirect('homepage:homepage-pasien')
                    
                else:
                    messages.error(request, 'Invalid username or password')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                context['login_forms'] = received_form
                return render(request, 'login.html', context)

def register(request):
    return render(request, 'register.html')

def register_admin(request):
    if request.method == "POST":
        form = AdminRegistration(request.POST)
        if form.is_valid():
            if is_user_not_exist(form):
                insert_admin(form)
                return HttpResponseRedirect(reverse("login:login"))
            else:
                messages.error(request, "Your ID Number or Email is already on database")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Your inputs are invalid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = AdminRegistration()
        context = {
            'form': form
        }
        return render (request, 'register-admin.html', context)

def insert_admin(form):
    user_data = [form.cleaned_data.get('email'), form.cleaned_data.get('username'), form.cleaned_data.get('password'), 
                    form.cleaned_data.get('name'), form.cleaned_data.get('id_number'),
                    form.cleaned_data.get('date_of_birth'),form.cleaned_data.get('address')]
    admin_data = [generate_employee_number(form.cleaned_data.get('date_of_birth')), form.cleaned_data.get('username'), '533-09-5091']
    with connection.cursor() as c:
        c.execute('INSERT INTO pengguna VALUES(%s, %s, %s, %s, %s, %s, %s)', user_data)
        c.execute('INSERT INTO administrator VALUES(%s, %s, %s)', admin_data)
                

def register_doctor(request):
    if request.method == "POST":
        form = DoctorRegistration(request.POST)
        if form.is_valid():
            if is_user_not_exist(form):
                insert_doctor(form)
                return HttpResponseRedirect(reverse("login:login"))			
            else:
                messages.error(request, "Your ID Number or Email is already exists")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Your inputs are invalid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = DoctorRegistration()
        context = {
            'form': form
        }
        return render (request, 'register-dokter.html', context)

def insert_doctor(form):
    user_data = [form.cleaned_data.get('email'), form.cleaned_data.get('username'), form.cleaned_data.get('password'), 
                    form.cleaned_data.get('name'), form.cleaned_data.get('id_number'),
                    form.cleaned_data.get('date_of_birth'),form.cleaned_data.get('address')]
    doctor_data = [generate_doctor_id(), form.cleaned_data.get('username'), form.cleaned_data.get('practice_license_number'), form.cleaned_data.get('specialty')]
    with connection.cursor() as c:
        c.execute('INSERT INTO pengguna VALUES(%s, %s, %s, %s, %s, %s, %s)', user_data)
        c.execute('INSERT INTO dokter VALUES(%s, %s, %s, %s)', doctor_data)

def register_patient(request):
    if request.method == "POST":
        form = PatientRegistration(request.POST)
        if form.is_valid():
            if is_user_not_exist(form):
                allergic_list = request.POST.getlist('alergi')
                insert_patient(form, allergic_list)
                return HttpResponseRedirect(reverse("login:login"))
            else:
                messages.error(request, "Your ID Number or Email is already exists")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Your inputs are invalid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = PatientRegistration()
        context = {
            'form': form
        }
        return render (request, 'register-pasien.html', context)

def insert_patient(form, list_of_alergi):
    user_data = [form.cleaned_data.get('email'), form.cleaned_data.get('username'), form.cleaned_data.get('password'), 
                    form.cleaned_data.get('name'), form.cleaned_data.get('id_number'),
                    form.cleaned_data.get('date_of_birth'),form.cleaned_data.get('address')]
    patient_data = [generate_medical_record_number(), form.cleaned_data.get('username'), "Flashpoint"]
    with connection.cursor() as c:
        c.execute('INSERT INTO pengguna VALUES(%s, %s, %s, %s, %s, %s, %s)', user_data)
        c.execute('INSERT INTO pasien VALUES(%s, %s, %s)', patient_data)
        for alergi in list_of_alergi:
            c.execute('INSERT INTO alergi_pasien VALUES(%s, %s)', [patient_data[0], alergi])

def is_user_not_exist(form):
    with connection.cursor() as c:
        c.execute('SELECT * FROM pengguna WHERE nomor_id = %s', [form.cleaned_data.get('no_identitas')])
        id_number = c.fetchall()
        
        if list(id_number):
            return False
        else:
            with connection.cursor() as c:
                c.execute('SELECT * FROM pengguna WHERE email = %s', [form.cleaned_data.get('email')])
                email = c.fetchall()
                if not(email):
                    return True
                else:
                    return False

def generate_employee_number(tanggal_lahir):
    year = tanggal_lahir.strftime("%Y")
    month = tanggal_lahir.strftime("%m")
    day = tanggal_lahir.strftime("%d")
    
    employee_number = year + month + day + str(random.randint(10000,1000000)) + str(random.randint(10000,1000000))
    return employee_number

def generate_doctor_id():
    with connection.cursor() as c:
        c.execute("SELECT id_dokter FROM dokter ORDER BY CAST(id_dokter AS INTEGER) DESC LIMIT 1")
        doctor_id = int(c.fetchone()[0]) + 1
    return str(doctor_id)

def generate_medical_record_number():
    medical_record_number = str(random.randint(1000,2000)) + "-"+ str(random.randint(10,100)) + "-" + str(random.randint(10,100))
    return medical_record_number
    
def logout(request):
    request.session.flush()
    messages.info(request, "You've been logged out")
    return redirect('/')
