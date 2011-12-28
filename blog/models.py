# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    # TODO: Defne fields here
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)
    #     verbose_name = _('BlogPost')
    #     verbose_name_plural = _('BlogPosts')

    # def __unicode__(self):
    #     pass
    
    # def save(self):
    #     pass
    
    # def get_absolute_url(self):
    #     pass
    
    # TODO: Defne custom methods here

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)    

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    
    