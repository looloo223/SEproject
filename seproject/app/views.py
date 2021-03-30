from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'app/base2.html')

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
def forumHealth(request):
    forums=forum.objects.filter(section="Health")
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':"Health"}
    return render(request,'forumHome.html',context)

@login_required
def forumPolicies(request):
    forums=forum.objects.filter(section="Policies")
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':"Policies"}
    return render(request,'forumHome.html',context)

@login_required
def forumOperations(request):
    forums=forum.objects.filter(section="Operations")
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':"Operations"}
    return render(request,'forumHome.html',context)

@login_required
def forumTechnologies(request):
    forums=forum.objects.filter(section="Technologies")
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':"Technologies"}
    return render(request,'forumHome.html',context)

@login_required
def forumGeneral(request):
    forums=forum.objects.filter(section="General")
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':"General"}
    return render(request,'forumHome.html',context)

@login_required
def forumSocial(request):
    forums=forum.objects.filter(section="Social")
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':"Social"}
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

@login_required
def forumDiscussion(request):
    if request.method=='GET':
        forumId = request.GET.get('topic')
        if not forumId:
            return render(request, 'forumDiscussion.html')
        else:
            forums=forum.objects.filter(topic=forumId)

            discussions=[]
            discussions.append(forums[0].discussion_set.all())

            form = CreateInDiscussion()

            context={'forum' : forums[0],
                    'discussions' : discussions,
                    'form' : form
                    }
            return render(request, 'forumDiscussion.html', context)

    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
                    form.save()
        return redirect('/forumMain/')






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
