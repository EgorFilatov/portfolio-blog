from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserForm, CustomUserContactForm
from .models import *
from .import urls
from user.models import *


class CreateUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/user_registration.html'
    success_url = reverse_lazy('home')



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
    if request.method == 'POST':
        form = CustomUserContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],  # subject
                form.cleaned_data['message'],  # message
                '23egih23@gmail.com',  # from email
                ['egor.filatov@live.com'],  # to email
            )

            return redirect('home')
    else:
        form = CustomUserContactForm()
    return render(request, "user/user_contacts.html", {'form': form,})


class UpdateUser(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('home')




