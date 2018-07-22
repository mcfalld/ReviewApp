from django.shortcuts import render
#from django.http import HttpResponse

from .models import Reviews

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