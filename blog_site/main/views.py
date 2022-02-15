from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import *
from user.models import *

# Create your views here.
user = CustomUser.objects.get(first_name='Егор')
user_first_name = user.first_name
user_last_name = user.last_name
about = user.about
email = user.email


def home_page(request):
    return render(request, "main/home_page.html", {'first_name': user_first_name,
                                                   'last_name': user_last_name,
                                                   'email': email,})


class BlogNewsList(ListView):
    model = News
    template_name = 'main/blog.html'
    context_object_name = 'news'
    extra_context = {'first_name': user_first_name,
                     'last_name': user_last_name,}


class BlogNewsDetail(DetailView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'
    extra_context = {'first_name': user_first_name,
                     'last_name': user_last_name,}


def category(request, cat_id):
    news = News.objects.filter(category_id=cat_id)
    return render(request, "main/category.html", {'first_name': user_first_name,
                                                  'last_name': user_last_name,
                                                  'news': news,})