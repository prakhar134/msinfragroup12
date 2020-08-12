from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return HttpResponse("<h1>hello</h1>")

def dashboard(request):
    content = User.objects.all()
    return render(request, 'app/dashboard.html', {'content': content})

def Register(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'app/register.html', context)

def loginpage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
    form = UserCreationForm()
    content = {'form': form}
    return render(request, 'app/login.html', content)