from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from log import views



urlpatterns = [
    # 注册路由
    path('article/list/', views.article_list, name="article_list"),
    ]