"""reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from django.urls import include, path

from reviewapp import views

urlpatterns = [
    url(r'^$', include('reviewapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^reviews/', include('reviewapp.urls')),#anything that starts 'reviewapp/' gets passed
    #to the urls file in the reviewapp folder
    # url(r'^details/)', include 
    # url(r'^login/', include('reviewapp.urls')),
    # url(r'^login/$', views.login, name='login'),
    url(r'^ratings/', include('star_ratings.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logged_out/$', views.logout, name='logout'),
    url(r'^profile/$', include('reviewapp.urls'), name='profile'),
    # url(r'^profil/$', au)
    url('accounts/profile/',
         TemplateView.as_view(template_name='accounts/profile.html'),
         name='profile'),   
    url('accounts/createReview/',
         TemplateView.as_view(template_name='accounts/createReview.html'),
         name='create_review'),   
]
