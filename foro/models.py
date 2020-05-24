from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Foro(models.Model):
    
    # id_foro = models.IntegerField(primary_key=True, default=1)
    nombre_foro = models.CharField(max_length=50, unique=True, default='Foro')
    descripcion_foro = models.CharField(max_length=100, default='Un foro de foroverflow')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    foto_foro = models.ImageField(upload_to='forum_pics', default='')

    def __str__(self):
        return self.nombre_foro


class Post(models.Model):

    # id_post = models.IntegerField(primary_key=True, default=1)
    id_foro = models.ForeignKey(Foro, on_delete=models.CASCADE, default=1)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200,default='')
    content = models.TextField(default='')

    def __str__(self):
        return self.title


class Comentario(models.Model):

    # id_comentario = models.IntegerField(primary_key=True, default=1)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE , default=1)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    contenido_comentario = models.TextField(default='')
    votos_comentario = models.IntegerField(default=0)

    def __str__(self):
        return self.id_comentario