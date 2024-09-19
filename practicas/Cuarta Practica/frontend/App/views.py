from django.shortcuts import render, redirect
from django.contrib import messages
import requests

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        academic_id = request.POST.get('academic_id')
        password = request.POST.get('password')

        # Datos para enviar al backend de Flask
        data = {
            'registroA': academic_id,
            'password': password
        }
# URL del endpoint de registro en Flask
        url = 'http://localhost:4000/usuarios/login'
        # Hacer la solicitud POST al backend de Flask
        response = requests.post(url, json=data)

        if response.status_code == 200:
            messages.success(request, 'Login exitoso.')
            # Redirigir a la página principal o a una página de usuario
            return redirect('index')
        elif response.status_code == 400:
            messages.error(request, 'Contraseña incorrecta.')
        elif response.status_code == 404:
            messages.error(request, 'Usuario no encontrado.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        academic_id = request.POST.get('academic_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # URL del endpoint de registro en Flask
        url = 'http://localhost:4000/usuarios/registrar'

        # Datos para enviar al backend de Flask
        data = {
            'registroA': academic_id,
            'nombre': first_name,
            'apellido': last_name,
            'email': email,
            'password': password
        }

        # Hacer la solicitud POST al backend de Flask
        response = requests.post(url, json=data)

        if response.status_code == 200:
            messages.success(request, 'Registro exitoso.')
            return redirect('login')  # Redirige a la página de login después del registro
        else:
            messages.error(request, 'Error al registrar el usuario.')

    # En caso de GET request o si ocurre un error en POST
    return render(request, 'register.html')
