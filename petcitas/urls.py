from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from petcitas import views

urlpatterns = [
     
     # API ESPECIALIDAD
     re_path(r'^especialidad_lista/$', views.EspecialidadLista.as_view() ),
     # API TYPES  
     re_path(r'^type_lista/$', views.TypeLista.as_view() ),

     
     # API CITAS
     re_path(r'^cita_lista/$', views.CitaLista.as_view() ),
     re_path(r'^cita_detalles/(?P<id>\d+)$', views.CitaDetalles.as_view() ),
     #API MASCOTAS 
     re_path(r'^mascota_lista/$', views.MascotaLista.as_view() ),
     re_path(r'^mascota_detalles/(?P<id>\d+)$',views.MascotaDetalles.as_view() ),


         
]

