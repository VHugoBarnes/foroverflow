from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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


def prueba(request):

    return render(request, 'usuario/base.html', {'title':'Prueba XD'})


@login_required
def user_profile(request):

    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('user-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        user_posts = Post.objects.filter(id_usuario=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': user_posts,
    }

    return render(request, 'usuario/profile/profile.html', context)