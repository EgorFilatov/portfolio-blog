from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm
from .models import *
from .import urls
from user.models import *


def home_page(request):
    return render(request, "main/home_page.html", {})


class BlogNewsList(ListView):
    model = News
    template_name = 'main/blog.html'
    context_object_name = 'news'
    extra_context = {}


def category(request, cat_id):
    news = News.objects.filter(category_id=cat_id)
    return render(request, "main/category.html", {'news': news,})


class BlogNewsDetail(DetailView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'
    extra_context = {}


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'main/news_add.html'
    success_url = reverse_lazy('blog')


