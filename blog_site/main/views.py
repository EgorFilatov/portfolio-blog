from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

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


class BlogNewsDetail(DetailView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'
    extra_context = {}


def category(request, cat_id):
    news = News.objects.filter(category_id=cat_id)
    return render(request, "main/category.html", {'news': news,})


def news_add(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('blog')
        else:
            error = 'error'
    else:
        form = NewsForm()
    return render(request, "main/news_add.html", {'form': form,
                                                  'error': error,})