from django.db import models



class Usuario(models.Model):
    nombre= models.CharField(null=False, max_length=100)
    email = models.CharField(max_length=1000 , null=False)
    contrasenia = models.CharField(max_length=1000 , null=False)
    delete = models.BooleanField(default = False)

    class Meta:
        db_table = "usuario"

class Denuncia(models.Model):
    titulo = models.CharField(null=False, max_length=100)
    descripcion = models.TextField(max_length=1000 ,null=False)
    imagen = models.ImageField(upload_to='media/', null=True)
    date_joined = models.DateField(null = False)
    delete = models.BooleanField(default = False)
    re_usuario= models.ForeignKey(Usuario, related_name='denuncias', on_delete=models.CASCADE)#null=false

    class Meta:
        db_table = "denuncia"

class Imagen(models.Model):
     imagen = models.ImageField(upload_to='media/', null=True)
     relacion_usuario=models. IntegerField()

     class Meta:
        db_table = "imagen"






