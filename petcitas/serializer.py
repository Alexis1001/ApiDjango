from rest_framework import routers, serializers, viewsets
from petcitas.models import Mascota
from petcitas.models import Cita
from petcitas.models import Especialidad
from petcitas.models import Type


class MascotaSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Mascota
        fields = ('__all__')

class CitaSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Cita
        fields = ('__all__')

class EspecialidadSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Especialidad
        fields = ('__all__')


class TypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('__all__')


        






