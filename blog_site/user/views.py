from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserForm
from .models import *
from .import urls
from user.models import *


def user_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_update')
    else:
        form = CustomUserCreationForm()
    return render(request, "user/user_registration.html", {'form': form,})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, "user/user_login.html", {'form': form,})


def user_logout(request):
    logout(request)
    return redirect('home')


def contacts(request):
    return render(request, "user/user_contacts.html", {})


class UpdateUser(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('home')




