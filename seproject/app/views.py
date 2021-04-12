from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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

def faq(request):
    return render(request, 'app/faq.html')

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
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():

            searchTerm = form.cleaned_data['search']
            forums = forum.objects.all()
            discussions=[]
            likes=[]
            count = 0
            
            for i in forums:
                
                if contains(i.topic, searchTerm):
                    discussions.append(i)
                    likes.append(i.totalLikes)
                    count += 1
            context={'forums':forums,
                'count':count,
                'discussions':discussions,
                'likes': likes,
                'searchTerm':searchTerm
                }
            return render(request, 'search.html', context)
    context = {
        'form':form
    }
    return render(request, 'forumMain.html', context)

#View for displaying each sections
@login_required
def forumView(request, forumName):
    
    forums=forum.objects.filter(section=forumName)
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
    if request.method =="POST":
        sortform = SortForm(request.POST)
        sortBy = sortform.data['sortBy']
    else:
        sortBy = "newest"
    forums = sortForum(forums, sortBy)
    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'section':forumName,
              }
    return render(request,'forumHome.html',context)

@login_required
def forumHome(request):
    forums=forum.objects.filter(section="Health")
    count=forums.count()
    discussions=[]
    discussionIndex = 0
    for i in forums:
        discussions.append(i.discussion_set.all())
        discussionIndex += 1

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'discussionIndex': discussionIndex,
              }
    return render(request,'forumHome.html',context)

@login_required
def addInForum(request, forumName):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            model=form.save(commit=False)
            model.name=auth.get_user(request).username
            model.section=forumName
            model.save()
            return redirect('forumMain') #the string used to be forumHome
    context ={'form':form,
                'forumName' : forumName}
    return render(request,'addInForum.html',context)

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
    totalLikes = myForum.totalLikes()

    liked = False
    if myForum.forumLikes.filter(id=request.user.id).exists():
        liked = True

    context={'forum' : myForum,
            'discussions' : discussions,
            'form' : form,
            'forumName' : forumName,
            'forumTopic' : forumTopic,
            'totalLikes' : totalLikes,
            'liked' : liked,
            }
    return render(request, 'forumDiscussion.html', context)

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
def LikeView(request, forumTopic):
    post=get_object_or_404(forum, topic= request.POST.get('post_id'))
    liked = False
    if post.forumLikes.filter(id=request.user.id).exists():
        post.forumLikes.remove(request.user)
        liked = False
    else:
        post.forumLikes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('forumDiscussion', args=[post.section, str(forumTopic)]))

@login_required
def userDiscussions(request):
    
    forums=forum.objects.filter(name=request.user)
    count=forums.count()
    discussions=[]
    likes=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
        likes.append(i.totalLikes)

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'likes': likes
              }
    return render(request, 'userDiscussions.html', context)

@login_required
def searchView(request):
    

    return render(request, 'search.html')

def sortForum(forums, sortBy):
    
    if sortBy == "newest":
        forums = sortNew(forums)
    elif sortBy == "likes":
        forums = sortLikes(forums)  
    #no sort is needed if a oldest is selected as the query returns a list that is already oldest to newest
    return forums

######################### Forum End ########################################

def contains(string, substring):
    num = 0
    match = False
    string = string.lower()
    substring = substring.lower()

    for letter in string:
        if letter == substring[num]:
            num += 1
        if num == len(substring):
            match = True
            break
    return match

def sortNew(forums):
    
    tempArray = []
    newArray = []
    while len(tempArray) < len(forums):
        newest = forums[0]
        for item in forums:
            if item.date_created > newest.date_created:
                if item.date_created not in tempArray:
                    newest =item
        tempArray.append(newest.date_created)
    
    for item in tempArray:
        for discussion in forums:
            if item == discussion.date_created:
                newArray.append(discussion)
    return newArray

def sortLikes(forums):
    newArray = []
    likeArray = []
    for item in forums:
        likeArray.append(item.totalLikes())
    likeArray = removeDuplicates(likeArray)
    likeArray.sort(reverse=True)
    for num in likeArray:
        for item in forums:
            if item.totalLikes() == num:
                newArray.append(item)
    return newArray

def removeDuplicates(array):
    tempArray = []
    for item in array:
        if item not in tempArray:
            tempArray.append(item)
    return tempArray
