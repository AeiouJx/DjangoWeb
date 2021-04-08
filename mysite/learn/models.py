

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Information(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    