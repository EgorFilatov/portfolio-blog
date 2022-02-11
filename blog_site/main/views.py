from django.shortcuts import render, redirect
from .models import *
from user.models import *

# Create your views here.
user = CustomUser.objects.get(first_name='Егор')
user_first_name = user.first_name
user_last_name = user.last_name
about = user.about


def home_page(request):
    return render(request, "main/home_page.html", {'first_name': user_first_name,
                                                   'last_name': user_last_name,})

def blog(request):
    return render(request, "main/blog.html", {'first_name': user_first_name,
                                              'last_name': user_last_name,
                                              'about': about,})
