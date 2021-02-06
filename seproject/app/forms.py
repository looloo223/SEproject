from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# creates a new version of login form that includes email
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']