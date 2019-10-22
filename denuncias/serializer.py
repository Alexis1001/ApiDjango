from rest_framework import routers, serializers, viewsets
from denuncias.models import Usuario
from denuncias.models import Denuncia
from denuncias.models import Imagen

class UsuarioSerializers(serializers.ModelSerializer):
    denuncias = serializers.SlugRelatedField(many=True,read_only=True,slug_field='titulo')
    #denuncias =serializers.SlugRelatedField(many=True,read_only=True,slug_field='descripcion')
    #denuncias =serializers.StringRelatedField(many=True)
    #no sirvio denuncias= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Usuario
        fields = ('__all__')
        #no sirvio fields = ('titulo','descripcion') 
        #no sirvio fields = ('titulo', 'denuncias')

class DenunciaSerializers(serializers.ModelSerializer):
    nombreUsuario =serializers.ReadOnlyField(source='re_usuario.nombre')
    emailUsuario=serializers.ReadOnlyField(source='re_usuario.email')
    #nameExample2 = serializers.ReadOnlyField(source='example.name')
    #deleteExample2 = serializers.ReadOnlyField(source='example.delete')
    class Meta:
        model = Denuncia
        fields = ('__all__')

#class ImagenSerializers(serializers.ModelSerializer): No sirvio
    #nombreUsuario =serializers.ReadOnlyField(source='re_usuario.nombre')
    #emailUsuario=serializers.ReadOnlyField(source='re_usuario.email')
    #nameExample2 = serializers.ReadOnlyField(source='example.name')
    #deleteExample2 = serializers.ReadOnlyField(source='example.delete')
 #   class Meta:
  #      model = Imagen
   #     fields = ('__imagen__')


