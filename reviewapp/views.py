from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import generic
from django.views.generic import View
from .forms import UserForm, UserReview
from ipware import get_client_ip
from django.template import loader

from .models import Reviews
from .models import Login

# Create your views here.
def index(request):
    #return HttpResponse("hello from reviewapp")
    # template = loader.get_template('reviewapp/index.html')
    reviews = Reviews.objects.all()

    context = {
            'title': 'Latest Reviews',
            'reviews': reviews
        }
    return render(request, 'reviewapp/index.html', context)
    # return HttpResponse(template.render(context, request))

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

    return render(request, 'reviewapp/login.html')

def profile(request):
    reviews = Reviews.objects.all() #user=request.user
    template = loader.get_template('reviewapp/profile.html')
    # review = Reviews.objects.filter(owner=get_current_user())

    context = {
        'title': 'Your Reviews',
        'reviews': reviews
    }

    return render(request, 'reviewapp/profile.html', context)

def logout(request):
    # template = loader.get_template('reviewapp/logged_out.html')
    auth.logout(request)
    return render(request, 'reviewapp/logged_out.html')
    # return HttpResponse(template.render(request))

def create_review(request):

    reviews = Reviews.objects.all()[:20]

    context = {
        'title': 'Your Reviews',
        'reviews': reviews
    }

    return render(request, 'reviewapp/createReview.html', context)

def create_user(request):

    user_info = Login.objects.all()

    context = {
        'user_info' : user_info,
        'title'     : Login.User_Name

    }

    return render(request, 'registration.backends.simple.urls', context)


# ip, is_routable = get_client_ip(request)
#     if ip is None:
#     ip = 0.0.0.0
#     else:
#         # We got the client's IP address
#         if is_routable:
#             # The client's IP address is publicly routable on the Internet
#         else:


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, '/registration/signup.html', {'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = 'reviewapp/signup.html'

    def get(self, request):
        form= self.form_class(None)
        return render(request, self.template_name, {'form' : form})

        #user submits user info
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('reviewapp/profile')

class ReviewForm(View):
    form_class = UserReview
    template_name = 'reviewapp/createReview.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        # if form.is_valid():
        review = form.save(commit=False)

        title = form.cleaned_data['title']
        body  = form.cleaned_data['body'] 
        submitted_on = form.cleaned_data['submitted_on']
        company = form.cleaned_data['company']
        reviewer_Email = form.cleaned_data['reviewer_Email']
        user = form.cleaned_data['user']

        review.save()

    