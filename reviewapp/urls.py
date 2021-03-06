from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

# from reviewapp.core import views as core_views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), #'reviews/' -> meaning there is nothing after the '/'    # checks views.py file for a method named index
    url(r'^reviews/$', views.IndexView.as_view(), name='reviews'), #'reviews/' -> meaning there is nothing after the '/'    # checks views.py file for a method named index
    url(r'^details/(?P<pk>\d+)/$', views.DetailView.as_view(), name='details'),
    # url(r'^login/$', views.login, name='login')
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^reviewapp/review-create/$', views.ReviewCreate.as_view(), name='review-create'),
    url(r'^reviews/reviewapp/review-create/$', views.ReviewCreate.as_view(), name='review-create'),
    url(r'^reviewapp/register/$', views.UserFormView.as_view(), name='register'),
    # url(r'')
    # url(r'^accounts/register$', , name='createReview'),
    # url(r'^signup/$', views.signup, name='signup'),
    
    # url(r'^)
]
