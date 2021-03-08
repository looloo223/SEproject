"""seproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from app.views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('health/', health),
    path('contact/', contact),
    path('operation/', operation, name='operation'),
    path('policies/', policies),
    path('register/', register),
    path('login/', loginPage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('operation/budgets/', RedirectView.as_view(url='https://bursar.columbusstate.edu/fees.php')),
    path('operation/campu/', RedirectView.as_view(url='https://students.columbusstate.edu/campus-life.php')),
    path('operation/orient/', RedirectView.as_view(url='https://orientation.columbusstate.edu')),
    path('operation/calendar/', RedirectView.as_view(url='https://academics.columbusstate.edu/calendars/')),
    path('operation/dining/', RedirectView.as_view(url='https://columbusstate.campusdish.com')),
    path('operation/rec/', RedirectView.as_view(url='https://campusrec.columbusstate.edu')),

    ######################## Forum #################################
    path('forumMain/',forumMain,name='forumMain'),
    path('forumHome/',forumHome,name='forumHome'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
    path('forumMain/forumHealth/',forumHealth,name='forumHealth'),
    path('forumMain/forumPolicies/',forumPolicies,name='forumPolicies'),
    path('forumMain/forumOperations/',forumOperations,name='forumOperations'),
    path('forumMain/forumTechnologies/',forumTechnologies,name='forumTechnologies'),
    path('forumMain/forumGeneral/',forumGeneral,name='forumGeneral'),
    path('forumMain/forumSocial/',forumSocial,name='forumSocial'),
    #path('forumMain/forumHealth/forumDiscussion/',forumDiscussion,name='forumDiscussion'),
    re_path(r'^forumMain/\w+/forumDiscussion/$',forumDiscussion,name='forumDiscussion'),
    #the above line fixed a bug that didn't allow the discussions in topics other than health to be viewed
     ####################### Forum ################################
]
