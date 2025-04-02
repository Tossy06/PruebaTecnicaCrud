from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('servers/add/', views.server_create, name='server_create'),
    path('servers/delete/<int:server_id>/', views.server_delete, name='server_delete'),
    path('servers/status/<int:server_id>/<str:status>/', views.server_change_status, name='server_change_status'),
    path('logout/', views.user_logout, name='logout'),
]