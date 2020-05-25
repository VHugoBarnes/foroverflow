from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Post, Foro
from .forms import PostForm


@login_required
def home(request):

    context = {
        'posts': Post.objects.all().order_by('-pk'),
        'foros': Foro.objects.all(),
        'user': request.user.username,
    }
    return render(request, 'foro/home.html', context)


@login_required
def post_detail(request, forum, id):

    print("="*60)
    print("ENTRO AL METODO POST_DETAIL")
    print("="*60)

    post = Post.objects.get(pk=id)
    forum = Foro.objects.get(nombre_foro=forum)

    print("="*60)
    print("ENTRO AL METODO POST_DETAIL")
    print("="*60)

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
            post.save()
            return redirect('post-detail', forum=post.id_foro, id=post.id)

    else:

        form = PostForm()

    context = {
        'form': form,
        'requested_user': request.user,
    }

    return render(request, "foro/create-post.html", context)


@login_required
def edit_post(request, forum, id):

    print("="*60)
    print("ENTRO AL METODO EDIT_POST")
    print("="*60)

    post = get_object_or_404(Post, pk=id)
    
    if request.user == post.id_usuario:
        if request.method == 'POST':
            
            form = PostForm(request.POST, instance=post)

            if form.is_valid():
                post = form.save(commit=False)
                post.id_usuario = request.user
                post.save()
                return redirect('post-detail', forum=post.id_foro, id=post.pk)
        else:
            form = PostForm(instance=post)
        context = {
            'post':Post.objects.get(pk=id),
            'form': form,
            'requested_user': request.user,
        }
        return render(request, "foro/edit-post.html", context)
    else:
        return redirect('home')

@login_required
def delete_post(request, id):

    post = Post.objects.get(pk=id)

    if request.user == post.id_usuario:
        if request.method == 'POST':
            print("="*60)
            print("ENTRO AL METODO POST")
            print("="*60)
            post.delete()
            return redirect('home')
        
        context = {
            'post':Post.objects.get(pk=id),
            'requested_user': request.user,
        }
        return render(request, "foro/delete-post.html", context)
    else:
        return redirect('home')


@login_required
def foro(request, forum):

    print("="*60)
    print("ENTRO AL METODO FORO")
    print("="*60)

    foro = get_object_or_404(Foro, nombre_foro=forum)
    posts = Post.objects.filter(id_foro=foro).order_by('-pk')
    forum = Foro.objects.get(nombre_foro=forum)
    print("="*60)
    print(forum)
    print(posts)
    print("="*60)

    context = {
        'forum': forum,
        'user': request.user,
        'posts': posts, 
    }

    return render(request, "foro/forum.html", context)

