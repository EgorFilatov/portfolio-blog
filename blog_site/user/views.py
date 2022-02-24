from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm
from .models import *
from .import urls
from user.models import *


def user_registration(request):
    form = CustomUserCreationForm()
    return render(request, "user/user_registration.html", {'form': form,})

def user_login(request):
    return render(request, "user/user_login.html", {})





