from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record



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
            return redirect('home')
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


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'Você precisa estar logado para visualizar os dados')
        return redirect('home')     

def view_database(request):
    records = Record.objects.all()
    return render(request, 'database.html', {'records':records})

def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer_id = Record.objects.get(id=pk)
        # customer_id.delete()
        messages.success(request, 'Usuário deletado com sucesso!')
        return redirect('home')
    else:
        messages.success(request, 'Somente o admin pode deletar')
        return redirect('home')
    
def add_customer(request):
    return render(request, 'add_customer.html', {})
