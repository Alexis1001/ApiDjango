from django.db import models


class Mascota(models.Model):
    name=models.CharField(null=False,max_length=100)
    birth_date=models.DateField(null=False)
    type_id=models.IntegerField(null=False)
    owner_id=models.IntegerField()
    delete = models.BooleanField(default = False)   

    class Meta:
        db_table="pet"

class Cita(models.Model):
    owner_id=models.IntegerField()
    fecha= models.DateField(null = False)
    hora=models.CharField(null=False,max_length=100)
    mascota=models.IntegerField()
    especialidad=models.IntegerField()
    delete = models.BooleanField(default = False)

    class Meta:
        db_table="cita"


class Especialidad(models.Model):
    nombre=models.CharField(null=False,max_length=100)
    delete = models.BooleanField(default = False)

    class Meta:
        db_table="especialidad"


class Type(models.Model):
    name=models.CharField(null=False,max_length=100)
    delete=models.BooleanField(default=False)

    class Meta:
        db_table="type"














