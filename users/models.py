from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True),
    email = models.CharField(max_length=254, unique=True),
    password = models.CharField(max_length=128, ),

    def __str__(self):
        return self.username
    
class Server(models.Model):
    OS_CHOICES = [
        ('Windows Server', 'Windows Server'),
        ('Ubuntu', 'Ubuntu'),
        ('CentOS', 'CentOS'),
        ('Debian', 'Debian'),
        ('Otros', 'Otros'),
    ]

    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Mantenimiento', 'Mantenimiento'),
    ]

    name = models.CharField(max_length=100, unique=True)
    operating_system = models.CharField(max_length=50, choices=OS_CHOICES)
    ram = models.IntegerField(help_text="Memoria RAM en GB")
    storage = models.FloatField(help_text="Capacidad del disco en GB")
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Activo')

    def __str__(self):
        return f"{self.name} - {self.status}"