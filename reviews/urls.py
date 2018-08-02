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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from reviewapp import views

# from reviewapp.core import views as core_views
# from django.urls import include, path

# from reviewapp/views import logout

urlpatterns = [
    url(r'^$', include('reviewapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^reviews/', include('reviewapp.urls')),#anything that starts 'reviews/' gets passed
    #to the urls file in the reviewapp folder
    # url(r'^details/)', include 
    url(r'^ratings/', include('star_ratings.urls')),
    # url(r'^login/$', auth_views.login, name='login'),
    url(r'^logged_out/$', views.logout, name='logout'),
    url(r'^create-review/$', include('reviewapp.urls'), name='profile'),
    # url(r'^profil/$', au)
    url('profile/',
         TemplateView.as_view(template_name='reviewapp/profile.html'),
         name='profile'),
    url(r'^login/$', auth_views.login,
        {'template_name':'reviewapp/login.html'},
        name='login'),
    url(r'^reviewapp/review-create/$', views.ReviewCreate.as_view(), name='review-create'),
    url(r'^reviewapp/register/$', views.UserFormView.as_view(), name='register'),
    # url('createReview/',
    #      TemplateView.as_view(template_name='reviewapp/createReview.html'),
    #      name='create_review'),   
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^registration/create_user/$', include('registration.backends.simple.urls')),
    # url(r'^signup/$', views.signup, name='signup'),
    # url('signup/',
    #      TemplateView.as_view(template_name='reviewapp/signup.html'),
    #      name='signup'),
    # url(r'^signup/', views.CreateUser.as_view(), name = 'signup'),
    # url('create_user/',
    #      TemplateView.as_view(template_name='reviewapp/signup.html'),
    #      name='create_user'),


]
