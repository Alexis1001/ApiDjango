from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from denuncias import views

urlpatterns = [
     re_path(r'^usuario_lista/$', views.UsuarioLista.as_view() ),
     re_path(r'^usuario_detalles/(?P<id>\d+)$', views.UsuarioDetalles.as_view() ),

     # Ulrs denuncia
     re_path(r'^denuncia_lista/$', views.DenunciaLista.as_view() ),
     re_path(r'^denuncia_detalles/(?P<id>\d+)$', views.DenunciaDetalles.as_view() ),

          
]

