from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import Http404

from denuncias.models import Denuncia
from denuncias.models import Usuario
#from denuncias.models import Imagen

from denuncias.serializer import  DenunciaSerializers
from denuncias.serializer import UsuarioSerializers
#from denuncias.serializer import ImagenSerializers



#class ImagenCreate(APIView):
#	serializer_class = ImagenSerializer
#	queryset = Imagen.objects.all()



class UsuarioLista(APIView):
    
    def get(self, request, format=None):
        queryset = Usuario.objects.filter(delete=False)
        serializer = UsuarioSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UsuarioSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UsuarioDetalles(APIView):
    def get_object(self, id):
        try:
            return Usuario.objects.get(pk=id, delete=False)
        except Usuario.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario != False:
            serializer = UsuarioSerializers(usuario)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Usuario.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario != False:
            serializer = UsuarioSerializers(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Preparando a denuncias    

class DenunciaLista(APIView):
    
    def get(self, request, format=None):
        queryset = Denuncia.objects.filter(delete=False)
        serializer = DenunciaSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DenunciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DenunciaDetalles(APIView):

    def get_object(self, id):
        try:
            return Denuncia.objects.get(pk=id, delete=False)
        except Denuncia.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        denuncia = self.get_object(id)
        if denuncia != False:
            serializer = DenunciaSerializers(denuncia)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Denuncia.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        denuncia = self.get_object(id)
        if denuncia != False:
            serializer = DenunciaSerializers(denuncia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

        

    



    








