from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm



def home(request):

    return render(request, 'home.html', {})

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('login')
        else:
            messages.success(request, 'Login failed. Please try again.')
            return redirect('login')
        
    return render(request, 'login.html', {})

def logout_user(request):

    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')


def register_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso. Seja bem-vindo!')
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})



