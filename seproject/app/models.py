from django.db import models
from django.forms import ModelForm

# Create your models here.

############################## Forum ##################################

class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    topic= models.CharField(max_length=300, unique=True)
    section = models.CharField(max_length=12)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    likeCount = models.IntegerField(default=0)
    dislikeCount = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,default="General",on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    name=models.CharField(max_length=200,default="anonymous" )
 
    def __str__(self):
        return str(self.forum)
        

class Likes(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    user = models.CharField(max_length=300, unique=True)

class Dislikes(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    user= models.CharField(max_length=300, unique=True)

############################ Forum #################################