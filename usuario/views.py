from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from usuario.forms import RegistrationForm


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