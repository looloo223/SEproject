from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.models import inlineformset_factory
from django.forms.widgets import Textarea
from django.utils.translation import gettext_lazy as _
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
    

    class Meta:
        model= Discussion
        fields = ["discuss"]
        widgets = {
            'discuss' : Textarea(attrs={'cols': 40, 'rows': 10}),
        }
        labels = {
            'discuss' : _('')
        }

DiscussionFormset = inlineformset_factory(forum, Discussion, fields=('discuss',))

class replyForm(forms.Form):
    reply = forms.CharField(label="Reply", max_length=1000)
        

