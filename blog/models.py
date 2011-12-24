# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    # TODO: Defne fields here
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    # class Meta:
    #     verbose_name = _('BlogPost')
    #     verbose_name_plural = _('BlogPosts')

    # def __unicode__(self):
    #     pass
    
    # def save(self):
    #     pass
    
    # def get_absolute_url(self):
    #     pass
    
    # TODO: Defne custom methods here

admin.site.register(BlogPost)    