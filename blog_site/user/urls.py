from django.contrib import admin
from django.urls import path, include
from .import views
from .views import *

urlpatterns = [
    path('user/register', views.user_registration, name='user_registration'),
    path('user/login', views.user_login, name='user_login'),
    path('user/logout', views.user_logout, name='user_logout'),

]