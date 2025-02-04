"""
URL configuration for exposicao_venda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_site.urls')),
    path('cliente/', include('cliente.urls')),
    #path('fornecedor/', include('fornecedor.urls')),
    #path('produtos/', include('produtos.urls')),
    #path('compras/', include('compras.urls')),
    #path('itens_compra/', include('itens_compra.urls')),
    #path('pagamento/', include('pagamento.urls'))
]
