# CRUD de Servidores con Django y SQLite3

## Descripción
Este proyecto es una aplicación web desarrollada en **Django** con una base de datos en **SQLite3** que permite gestionar servidores. Implementa un **CRUD** (Crear, Leer, Actualizar y Eliminar) para la administración de servidores y también cuenta con un sistema de registro y autenticación de usuarios.

La aplicación está dividida en dos apps:
- **`crud`**: Contiene la configuración principal del proyecto.
- **`users`**: Gestiona los servidores y la autenticación de usuarios.

## Tecnologías utilizadas
- **Python 3**
- **Django 5.2**
- **SQLite3**
- **Bootstrap 5** (para la interfaz)

## Estructura del proyecto
```
PRUEBATECNICA/
│── crud/              # Configuración del proyecto Django
│   │── settings.py    # Configuración general
│   │── urls.py        # Rutas principales
│   │── asgi.py        
│   │── wsgi.py        
│
│── users/             # Aplicación para gestión de servidores y usuarios
│   │── migrations/    # Migraciones de la base de datos
│   │── static/        # Archivos estáticos (CSS, etc.)
│   │── templates/     # Plantillas HTML
│   │── models.py      # Definición de la base de datos
│   │── views.py       # Lógica de negocio
│   │── urls.py        # Rutas de la app users
│
│── venv/              # Entorno virtual de Python
│── db.sqlite3         # Base de datos SQLite3
│── manage.py          # Archivo principal de Django
│── requirements.txt   # Dependencias del proyecto
```

## Instalación y configuración
### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones y ejecutar el servidor
```bash
python manage.py migrate
python manage.py runserver
```

## Uso
### Registro y autenticación de usuarios
- Los usuarios pueden registrarse e iniciar sesión para gestionar los servidores.

### Gestión de servidores
- **Crear** un nuevo servidor especificando nombre, sistema operativo, RAM, almacenamiento e IP.
- **Listar** servidores registrados.
- **Actualizar** el estado del servidor (Activo, Inactivo, Mantenimiento).
- **Eliminar** servidores.

## Captura de pantalla
![image](https://github.com/user-attachments/assets/71db9031-1161-46dc-ad46-20c9d847eb88)


## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

## Autor
Desarrollado por David Gómez.

