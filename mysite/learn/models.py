

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# django-ckeditor
from ckeditor.fields import RichTextField

class Information(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
    

class MyInfo(models.Model):
    title = models.CharField(max_length=128)
    body = RichTextField(config_name='my_config')
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Technology(models.Model):
    name = models.CharField(max_length=128)
    path = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.name
    
    
'''
雷霆加速器 g'f      2021-04-10

佛跳墙VPN fotiaoqiang.io      2021-04-10

富文本编辑器 https://github.com/django-ckeditor/django-ckeditor      2021-04-09

粘性侧边栏 https://github.com/abouolia/sticky-sidebar      2021-04-09

轻量级的标记语言Markdown： https://python-markdown.github.io/extensions/toc/      2021-04-08

Django验证系统重置密码: https://docs.djangoproject.com/zh-hans/2.1/topics/auth/default/      2021-04-08

Django分页模块: https://docs.djangoproject.com/zh-hans/2.1/topics/pagination/      2021-04-08

内网穿透： https://natapp.cn/#download      2021-04-08

矢量图标库： https://fontawesome.com/      2021-04-08
'''    
    
    
    
    
    
    
    
    
    
    
    