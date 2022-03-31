from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserForm, CustomUserContactForm
from .models import *
from .import urls
from user.models import *


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/user_registration.html'
    success_message = "Вы успешно зарегистрировались"

    def get_success_url(self):
        return reverse_lazy('user_login')


class LoginUser(LoginView):
    form_class = CustomUserLoginForm
    template_name = "user/user_login.html"

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('home')


def contacts(request):
    if request.method == 'POST':
        form = CustomUserContactForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Сообщение успешно отправлено!')
            message = 'Email от %s (%s): %s' % (form.cleaned_data['contact_name'], form.cleaned_data['contact_email'], form.cleaned_data['message'])
            send_mail(
                'Письмо из портфолио сайта',  # subject
                message,  # message
                '23egih23@gmail.com',  # from email
                ['egor.filatov@live.com'],  # to email
            )
            #return redirect('success_message')
    else:
        form = CustomUserContactForm()
    return render(request, "user/user_contacts.html", {'form': form,})


def success_message(request):
    return render(request, "user/success_message.html", {})


class UpdateUser(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('home')




