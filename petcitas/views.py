from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import Http404

from petcitas.models import Type
from petcitas.models import Especialidad
from petcitas.models import Cita
from petcitas.models import Mascota

from petcitas.serializer import TypeSerializers
from petcitas.serializer import EspecialidadSerializers
from petcitas.serializer import CitaSerializers
from petcitas.serializer import MascotaSerializers



#preparando el modelo especialidad 
class EspecialidadLista(APIView):
    
    def get(self, request, format=None):
        queryset = Especialidad.objects.filter(delete=False)
        serializer = EspecialidadSerializers(queryset, many=True)
        return Response(serializer.data)

#preparando el modelo types
class TypeLista(APIView):
    
    def get(self, request, format=None):
        queryset = Type.objects.filter(delete=False)
        serializer = TypeSerializers(queryset, many=True)
        return Response(serializer.data)

# preprando el modelo citas 

class CitaLista(APIView):

    def get(self, request, format=None):
        queryset = Cita.objects.filter(delete=False)
        serializer = CitaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

class CitaDetalles(APIView):

    def get_object(self, id):
        try:
            return Cita.objects.get(pk=id, delete=False)
        except Cita.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        cita = self.get_object(id)
        if cita != False:
            serializer = CitaSerializers(cita)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        cita = self.get_object(id)
        if cita != False:
            serializer = CitaSerializers(cita, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)   

#preparando el modelo mascotas 

class MascotaLista(APIView):
    def get(self, request, format=None):
        queryset = Mascota.objects.filter(delete=False)
        serializer = MascotaSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = MascotaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 


class MascotaDetalles(APIView):

    def get_object(self, id):
        try:
            return Mascota.objects.get(pk=id, delete=False)
        except Mascota.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        mascota= self.get_object(id)
        if mascota != False:
            serializer = MascotaSerializers(mascota)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        mascota = self.get_object(id)
        if mascota != False:
            serializer = MascotaSerializers(mascota, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)                   


  
    

