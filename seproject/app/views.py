from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# groups: Staff, Faculty, Health, Student, Technical
# to restrict a page to a specific group of users use following line:
# @allowed_users(allowed_roles=['Staff'])

def index(request):
    return render(request, 'app/index.html')

def health(request):
    return render(request, 'app/health.html')

def contact(request):
    return render(request, 'app/contact.html')

def operation(request):
    return render(request, 'app/operation.html')

def policies(request):
    return render(request, 'app/policies.html')

def technologies(request):
    return render(request, 'app/technologies.html')

def screener(request):
    return render(request, 'app/screener.html')

def register(request):
    form = UserCreationForm()                                           # Use CreateUserForm() for email entry as well
    if request.method == 'POST':
        form = UserCreationForm(request.POST)                           # Send in the data of the form
        if form.is_valid():                                             # Validate the data from the form
            user = form.save() #       used to be just form.save()                                          # Save new user to database
            # old line user = form.cleaned_data.get('username')
            login(request, user)   #logins in the user this was added 3/2/2021
            return redirect('home')             # old string was "/accounts/login"                       # redirect user to login page
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
def forumMain(request):
    return render(request, 'forumMain.html')

@login_required
def forumView(request, forumName):
    forums=forum.objects.filter(section=forumName)
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':forumName}
    return render(request,'forumHome.html',context)

@login_required
def forumHome(request):
    forums=forum.objects.filter(section="Health")
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
            return redirect('forumMain') #the string used to be forumHome
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

@login_required
def forumDiscussion(request, forumName, forumTopic):
    myForum=forum.objects.get(section=forumName, topic=forumTopic)
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.forum=myForum
            model=form.save(commit=False)
            model.name=auth.get_user(request).username
            model.forum=myForum
            model.save()
        return redirect('/forumMain/')

    discussions=[]
    discussions.append(myForum.discussion_set.all())

    form = CreateInDiscussion()

    context={'forum' : myForum,
            'discussions' : discussions,
            'form' : form,
            'forumName' : forumName,
            'forumTopic' : forumTopic
            }
    return render(request, 'forumDiscussion.html', context)

    






    #forums=forum.objects.filter(section="Health")
    #count=forums.count()
    ##discussions=[]
    ##for i in forums:
    ##    discussions.append(i.discussion_set.all())

    #context={'forums':forums,
    #          'count':count,
    #          #'discussions':discussions,
    #          'section':"Health"}
    #return render(request,'forumDiscussion.html',context)

    ########################## Forum End ########################################
