# -*- coding: utf-8 -*-
# learn/urls.py

# 引入path
from django.urls import path
# 引入views.py
from . import views

from django.http import HttpResponse
from django.conf.urls import include, url
# 正在部署的应用的名称
app_name = 'learn'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('info/', views.info, name='info'),
    path('msggate/',views.msgproc, name='msggate'),
    url('api/666', view=lambda request: HttpResponse('戏说不是胡说')),
]