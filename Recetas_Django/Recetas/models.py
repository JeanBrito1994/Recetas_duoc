from django.db import models

# Create your models here.
class usuario(models.Model):
    rut = models.IntegerField(primary_key=True, max_length=8)
    rut_dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'usuario'