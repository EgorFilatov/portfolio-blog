from django.contrib import admin
from django.urls import path, include
from .import views
from .views import *

urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/', BlogNewsList.as_view(), name='blog'),
    path('category/<int:cat_id>/', views.category, name='categories'),
    path('news/<int:pk>/', BlogNewsDetail.as_view(), name='news'),
    path('news_add/', views.news_add, name='news_add'),
]