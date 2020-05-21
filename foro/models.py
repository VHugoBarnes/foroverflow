from django.db import models
from django.utils import timezone
from usuario.models import Usuario

# Create your models here.
class Foro(models.Model):

    id_foro = models.IntegerField(primary_key=True)
    nombre_foro = models.CharField(max_length=50, unique=True)
    descripcion_foro = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    foto_foro = models.ImageField(upload_to='', default='')

    def __str__(self):
        return self.nombre_foro


class Post(models.Model):

    id_post = models.IntegerField(primary_key=True)
    id_foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo_post = models.CharField(max_length=200)
    contenido_post = models.TextField()
    votos_post = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo_post


class Comentario(models.Model):

    id_comentario = models.IntegerField(primary_key=True)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido_comentario = models.TextField()
    votos_comentario = models.IntegerField(default=0)

    def __str__(self):
        return self.id_comentario