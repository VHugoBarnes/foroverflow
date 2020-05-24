from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    UpdateView,
)

from .models import Post, Foro
from .forms import PostForm


@login_required
def home(request):

    context = {
        'posts': Post.objects.all(),
        'foros': Foro.objects.all(),
        'user': request.user.username,
    }
    return render(request, 'foro/home.html', context)


@login_required
def post_detail(request, forum, id):

    post = Post.objects.get(id_post=id)
    forum = Foro.objects.get(nombre_foro=forum)

    context = {
        'post': post,
        'forum': forum,
        'user': request.user,
    }

    return render(request, "foro/post_detail.html", context)


@login_required
def create_post(request):

    if request.method == 'POST':
        
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_usuario = request.user
            post.id_post = Post.objects.count()+1
            post.save()
            return redirect('post-detail', forum=post.id_foro, id=post.id_post)

    else:

        form = PostForm()

    context = {
        'form': form,
        'requested_user': request.user,
    }

    return render(request, "foro/create-post.html", context)


@login_required
def edit_post(request, forum, id):

    post = get_object_or_404(Post, id_post=id)

    if request.user == post.id_usuario:
        if request.method == 'POST':
            
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_usuario = request.user
                post.id_post = post.id_post
                post.save()
                return redirect('post-detail', forum=post.id_foro, id=post.id_post)
        else:
            form = PostForm(instance=post)
        context = {
        'form': form,
        'requested_user': request.user,
        }
        return render(request, "foro/create-post.html", context)
    else:
        return redirect('home')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['id_foro', 'title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requested_user'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.id_usuario = self.request.user
        return super().form_valid(form) and redirect('post-detail', forum=form.instance.id_foro, id=form.instance.id_post)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.id_usuario:
            return True
        return False
