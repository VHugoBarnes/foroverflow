from django.db import models

class Usuario(models.Model):
    
    id_usuario = models.IntegerField(primary_key=True, default=1)
    correo_usuario = models.EmailField(max_length=254, unique=True, default='')
    nombre_usuario = models.CharField(max_length=40, unique=True, default='')
    contraseña = models.CharField(max_length=60, default='')
    foto_usuario = models.ImageField(upload_to='media', default='')

    def __str__(self):
        return self.nombre_usuario