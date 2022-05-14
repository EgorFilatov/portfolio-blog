from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm
from .models import *
from .import urls
from user.models import *
from .parse import parsing


def home_page(request):
    return render(request, "main/home_page.html", {})


def category(request, pk):
    news = News.objects.filter(category_id=pk)
    category_name = Categories.objects.get(pk=pk)
    paginator = Paginator(news, 20)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "main/category.html", {'page_obj': page_obj,
                                                  'category_name': category_name,})

def parse(request):
    news_list = parsing()
    i = 0
    while i < len(news_list):
        news = News(header=news_list[i]['header'], annotation=news_list[i]['annotation'], full_text=news_list[i]['annotation'], category=Categories.objects.get(pk=7), image_url=news_list[i]['image'])
        news.save()
        i = i + 1
    return redirect('blog')


class BlogNewsList(ListView):
    paginate_by = 20
    model = News
    template_name = 'main/blog.html'
    extra_context = {}


class BlogNewsDetail(DetailView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'
    extra_context = {}


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'main/news_add.html'
    success_url = reverse_lazy('blog')
    login_url = 'user_login'


class UpdateNews(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'main/news_update.html'
    login_url = 'user_login'


class DeleteNews(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'main/news-delete.html'
    success_url = reverse_lazy('blog')
    login_url = 'user_login'

class Search(ListView):
    template_name = 'main/search.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        return News.objects.filter(header__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context






