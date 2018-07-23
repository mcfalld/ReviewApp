from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #'reviews/' -> meaning there is nothing after the '/'    # checks views.py file for a method named index
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    # url(r'^login/$', views.login, name='login')
    url(r'^profile/$', views.profile, name='profile')
]