from django.contrib import admin
from .models import Foro, Post, Comentario

# Register your models here.
admin.site.register(Foro)
admin.site.register(Post)
admin.site.register(Comentario)