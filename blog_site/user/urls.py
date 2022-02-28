from django.contrib import admin
from django.urls import path, include
from .import views
from .views import *

urlpatterns = [
    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('contacts/', views.contacts, name='contacts'),

]