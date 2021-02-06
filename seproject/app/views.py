from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

def index(request):
    return render(request, 'app/index.html')

def health(request):
    return render(request, 'app/health.html')
    
def contact(request):
    return render(request, 'app/contact.html')

def operation(request):
    return render(request, 'app/operation.html')

def register(request):
    form = UserCreationForm()                                           # Use CreateUserForm() for email entry as well
    if request.method == 'POST':
        form = UserCreationForm(request.POST)                           # Send in the data of the form
        if form.is_valid():                                             # Validate the data from the form
            form.save()                                                 # Save new user to database
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)# Show successful login
            return redirect('login')                                    # redirect user to login page
    context = {'form':form}
    return render(request, 'app/register.html', context)
	
def loginPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'app/login.html', context)