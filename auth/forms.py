from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {
        'class':'form-control',
        'placeholder':'',
            
    }),
    required = True)

    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class':'form-control',
        'placeholder':'',
    }),
    required = True)

class AdminRegistration(forms.Form):
    username = forms.CharField(label="username", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Masukkan username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Masukkan password'
    }))
    id_number = forms.CharField(label="id_number", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    name = forms.CharField(label="name", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
        'placeholder': 'Masukkan tanggal lahir'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    address = forms.CharField(label="address", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))

class DoctorRegistration(forms.Form):
    username = forms.CharField(label="username", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    id_number = forms.CharField(label="id_number", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    name = forms.CharField(label="nama", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Masukkan nama lengkap'
    }))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
        'placeholder': '',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    address = forms.CharField(label="alamat", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    practice_license_number = forms.CharField(label="practice_license_number", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    specialty = forms.CharField(label="specialty", max_length=50, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))

class PatientRegistration(forms.Form):
    username = forms.CharField(label="username", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Masukkan password'
    }))
    id_number = forms.CharField(label="id_number", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    name = forms.CharField(label="name", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
        'placeholder': '',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
    address = forms.CharField(label="address", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))
