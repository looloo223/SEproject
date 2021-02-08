from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

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
            return redirect('/accounts/login')                                    # redirect user to login page
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

def logout(request):
    logout(request)
    return redirect('home')

############################# Forum ########################################## 

@login_required
def forumHome(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'forumHome.html',context)

@login_required
def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forumHome')
    context ={'form':form}
    return render(request,'addInForum.html',context)

@login_required
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forumHome')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)

    ########################## Forum End ########################################