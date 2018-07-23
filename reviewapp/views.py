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
    
    
    # from ipware import get_client_ip

    # ip, is_routable = get_client_ip(request)
#     if ip is None:
#    # Unable to get the client's IP address
#         return None
#     else:
#     # We got the client's IP address
#         if is_routable:
#         # The client's IP address is publicly routable on the Internet
#             return ip
#         else:
#         # The client's IP address is private
#             return None


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
    reviews = Reviews.objects.all()[:25]

    context = {
        'headtitle'  : 'Your Reviews',
        'reviews' : reviews
    }

    return render(request, 'accounts/profile.html', context)

def logout(request):
    
    auth.logout(request)
    return render(request, 'registration/logged_out.html')

