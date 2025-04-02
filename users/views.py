from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.hashers import check_password, make_password

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

def home(request):
    user_name = request.session.get('user_name')  # Se obtiene de la sesión directamente
    
    if user_name:
        return render(request, 'home.html', {'user_name': user_name})
    else:
        messages.error(request, 'El nombre de usuario no está presente.')
        return redirect('register')
