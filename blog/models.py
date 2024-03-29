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
    genre = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title

    # class Meta:
        # abstract = True

#django.core.exceptions.FieldError: Local field 'authors' in class 'SimthBook' 
#clashes with field of similar name from base class 'Book'
# class SimthBook(Book):
    # authors = models.ManyToManyField(Author,limit_choices_to={
        # 'name__endswith':'Smith' })

class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['last','first','middle']
        unique_together = ['first','last','middle']
        verbose_name_plural = 'people'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'middle')

admin.site.register(Person, PersonAdmin)
        