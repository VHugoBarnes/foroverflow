from django.db import models

class Usuario(models.Model):

    id_usuario = models.IntegerField(primary_key=True)
    correo_usuario = models.EmailField(max_length=254, unique=True)
    nombre_usuario = models.CharField(max_length=40, unique=True)
    contraseña = models.CharField(max_length=60)
    foto_usuario = models.ImageField(upload_to='media', default='')

    def __str__(self):
        return self.nombre_usuario