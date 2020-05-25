from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from usuario.forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from foro.models import Post

from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, you can now login!')
            return redirect('login')
    else:
        form = RegistrationForm()
        
    return render(request, 'usuario/registro.html', {'form':form})


def prueba(request, profile):

    prof = User.objects.get(username=profile)

    return render(request, 'usuario/base.html', {'title':'Prueba XD'})


@login_required
def user_profile(request, user_name):

    user_name_ = User.objects.get(username=user_name)

    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('user-profile', user_name=user_name_)
    else:

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        user_posts = Post.objects.filter(id_usuario=user_name_).order_by('-pk')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': user_posts,
        'user': request.user,
        'requested_user': User.objects.get(username=user_name)
    }

    return render(request, 'usuario/profile/profile.html', context)