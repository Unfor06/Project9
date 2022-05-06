from .forms import CreationDeCompte
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout


User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CreationDeCompte(request.POST)
        if form.is_valid():

            if form.cleaned_data['captcha'] != '1234':
                form.add_error('captcha', 'Captcha invalide')
            else:
                form.save()
                return redirect('index')
    else:
        form = CreationDeCompte()
    return render(request, 'accounts/signup.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')
