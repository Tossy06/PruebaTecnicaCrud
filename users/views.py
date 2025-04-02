from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Server
from django.contrib import messages 
from django.contrib.auth.hashers import check_password, make_password
import re

def register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return render(request, 'register.html', {'username': username, 'email': email})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
            return render(request, 'register.html', {'username': username, 'email': email})

        try:
            encrypted_password = make_password(password)
            new_user = User.objects.create(username=username, email=email, password=encrypted_password)
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Ocurrió un error: {e}')
            return render(request, 'register.html', {'username': username, 'email': email})
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)  # Se corrige 'user_name' a 'username'

            if check_password(password, user.password):
                messages.success(request, 'Inicio de sesión exitoso')
                request.session['user_name'] = username  # Se guarda en la sesión
                return redirect('home')
            else:
                messages.error(request, 'Contraseña incorrecta')
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
            return redirect('register')
    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect('login')

def home(request):
    user_name = request.session.get('user_name')
    
    if user_name:
        servers = Server.objects.all()  # Obtener todos los servidores
        return render(request, 'home.html', {'user_name': user_name, 'servers': servers})
    else:
        messages.error(request, 'El nombre de usuario no está presente.')
        return redirect('register')
    
# Crear un servidor con validaciones mejoradas
def server_create(request):
    if request.method == 'POST':
        user_name = request.session.get('user_name')
        if not user_name:
            messages.error(request, 'Debes iniciar sesión para agregar un servidor.')
            return redirect('login')

        name = request.POST.get('name').strip()
        operating_system = request.POST.get('operating_system')
        ram = request.POST.get('ram')
        storage = request.POST.get('storage')
        ip_address = request.POST.get('ip_address').strip()
        status = request.POST.get('status')

        # Validaciones
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_address):
            messages.error(request, 'Dirección IP no válida.')
            return redirect('home')

        if not ram.isdigit() or not storage.isdigit():
            messages.error(request, 'RAM y Almacenamiento deben ser valores numéricos.')
            return redirect('home')

        if Server.objects.filter(name=name).exists():
            messages.error(request, 'El servidor ya existe.')
        else:
            Server.objects.create(
                name=name,
                operating_system=operating_system,
                ram=int(ram),
                storage=int(storage),
                ip_address=ip_address,
                status=status
            )
            messages.success(request, 'Servidor creado con éxito.')

        return redirect('home')

# Cambiar estado del servidor
def server_change_status(request, server_id, status):
    user_name = request.session.get('user_name')
    if not user_name:
        messages.error(request, 'Debes iniciar sesión para modificar servidores.')
        return redirect('login')

    server = get_object_or_404(Server, id=server_id)
    if status in dict(Server.STATUS_CHOICES):
        server.status = status
        server.save()
        messages.success(request, f"Estado cambiado a {status}.")
    return redirect('home')

# Eliminar servidor
def server_delete(request, server_id):
    user_name = request.session.get('user_name')
    if not user_name:
        messages.error(request, 'Debes iniciar sesión para eliminar servidores.')
        return redirect('login')

    server = get_object_or_404(Server, id=server_id)
    server.delete()
    messages.success(request, "Servidor eliminado con éxito.")
    return redirect('home')