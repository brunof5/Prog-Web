from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('', views.base_cliente, name='base_cliente'),
    path('<int:pk>/perfil/', views.perfil_cliente, name='perfil_cliente'),
    path('listar/', views.listar_clientes, name='listar_clientes'),
    path('criar/', views.criar_cliente, name='criar_cliente'),
    path('<int:pk>/atualizar/', views.atualizar_cliente, name='atualizar_cliente'),
    path('<int:pk>/deletar/', views.deletar_cliente, name='deletar_cliente')
]
