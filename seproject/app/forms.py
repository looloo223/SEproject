from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from .models import*

# creates a new version of login form that includes email
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CreateInForum(ModelForm):
    name = auth.__name__
    

    class Meta:
        model= forum
        fields = "__all__"
	
		
class CreateInDiscussion(ModelForm):
    #name = 'bob'
    #forum = forum.topic

    class Meta:
        model= Discussion
        fields = ["name","forum","discuss"]
        
        

