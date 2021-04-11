
# comment/models.py

from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost

# django-ckeditor
from ckeditor.fields import RichTextField

# 评论
class Comment(models.Model):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    # body = models.TextField()
    # 添加参数 config_name 指定使用的配置
    body = RichTextField(config_name='my_config')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
 





 