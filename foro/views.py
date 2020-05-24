from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Post, Foro
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)


@login_required
def home(request):

    context = {
        'posts': Post.objects.all(),
        'foros': Foro.objects.all(),
    }
    return render(request, 'foro/home.html', context)


@login_required
def post_detail(request, forum, id):

    post = Post.objects.get(id_post=id)
    forum = Foro.objects.get(nombre_foro=forum)

    context = {
        'post': post,
        'forum': forum,
    }

    return render(request, "foro/post_detail.html", context)
