from django.db import models
from django.forms import ModelForm
from .models import *
from django.contrib import admin

# Create your models here.

############################## Forum ##################################

class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    link = models.CharField(max_length=100 ,null =True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)

class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"

admin.site.register(forum)
admin.site.register(Discussion)

############################ Forum #################################