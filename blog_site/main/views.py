from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm
from .models import *
from .import urls
from user.models import *


def home_page(request):
    return render(request, "main/home_page.html", {})


class BlogNewsList(ListView):
    paginate_by = 5
    model = News
    template_name = 'main/blog.html'
    context_object_name = 'a'
    extra_context = {}


def category(request, cat_id):
    news = News.objects.filter(category_id=cat_id)
    category_name = Categories.objects.get(pk=cat_id)
    paginator = Paginator(news, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "main/category.html", {'page_obj': page_obj,
                                                  'category_name': category_name,})


class BlogNewsDetail(DetailView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'
    extra_context = {}


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'main/news_add.html'
    success_url = reverse_lazy('blog')


class UpdateNews(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'main/news_update.html'


class DeleteNews(DeleteView):
    model = News
    template_name = 'main/news-delete.html'
    success_url = reverse_lazy('blog')





