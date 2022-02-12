from django.contrib import admin
from django.urls import path, include
from .import views
from  .views import *

from .import views
from .views import *

urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/', BlogNewsShow.as_view(), name='blog'),
    path('category/<int:cat_id>/', views.category, name='categories'),

]