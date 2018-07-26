from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

from .models import Reviews
from .models import Login

# Create your views here.
def index(request):
    #return HttpResponse("hello from reviewapp")

    reviews = Reviews.objects.all()[:25]

    context = {
            'title': 'Latest Reviews',
            'reviews': reviews
        }
    return render(request, 'reviewapp/index.html', context)

def details(request, id):
    review = Reviews.objects.get(id=id)

    context = {
        'review': review
    }

    return render(request, 'reviewapp/details.html', context)


def login(request):
    
    # login = Login.objects.all()

    # context = {
    #     'login': login
    # }

    return render(request, 'registration/login.html')

def profile(request):
    # review = Reviews.objects.filter(owner=get_current_user())
    reviews = Reviews.objects.filter(user=request.user)[:25]

    context = {
        'title': 'Your Reviews',
        'reviews': reviews
    }

    return render(request, 'accounts/profile.html', context)

def logout(request):
    
    auth.logout(request)
    return render(request, 'registration/logged_out.html')

def create_review(request):

    reviews = Reviews.objects.all()[:20]

    context = {
        'title': 'Your Reviews',
        'reviews': reviews
    }

    return render(request, 'accounts/createReview.html', context)