from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('perfil/', views.perfil_cliente, name='perfil_cliente')
]