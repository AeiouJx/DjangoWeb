# -*- coding:utf-8 -*-
# iot/urls.py

# 引入path
from django.urls import path
from django.conf.urls import url, include
# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'iot'

urlpatterns = [
    path('index/', views.index, name='index'),
    url(r'add_book$', views.add_book, name='add_book'),
    url(r'show_books$', views.show_books, name='show_books'),
    
]