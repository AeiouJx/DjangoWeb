from django.contrib import admin

from .models import Information

# 注册ArticlePost到admin中
admin.site.register(Information)