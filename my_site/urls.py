from django.urls import path
from . import views

app_name = 'my_site'

urlpatterns = [
    path('', views.base_my_site, name='base_my_site')
]