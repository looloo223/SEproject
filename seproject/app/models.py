from django.db import models
from django.forms import ModelForm

# Create your models here.

############################## Forum ##################################

class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    topic= models.CharField(max_length=300)
    section = models.CharField(max_length=12)
    #section = models.ForeignKey(section,blank=False,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)



############################ Forum #################################