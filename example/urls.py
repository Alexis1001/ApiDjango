from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [
     re_path(r'^example_lista/$', views.ExampleList.as_view() ),
     re_path(r'^example_detail/(?P<id>\d+)$', views.ExampleDetail.as_view() ),
]