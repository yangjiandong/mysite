# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from mysite.utils.fields import ThumbnailImageField
 
# Create your models here.

class Item(models.Model):
  name = models.CharField(max_length=250)
  description = models.TextField()

  class Meta:
    ordering = ['name']

  def __unicode__(self):
    return self.name

  @models.permalink
  def get_absolute_url(self):
    return ('item_detail', None, {'object_id': self.id})

class Photo(models.Model):
  item = models.ForeignKey(Item)
  title = models.CharField(max_length=100)
  #image = models.ImageField(upload_to='photos')
  image = ThumbnailImageField(upload_to='photos')
  caption = models.CharField(max_length=200, blank=True)

  class Meta:
    ordering = ['title']

  def __unicode__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('photo_detail', None, {'object_id': self.id})

class PhotoInline(admin.StackedInline):
  model = Photo

class ItemAdmin(admin.ModelAdmin):
  inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)

class oo(object):
  """docstring for oo"""
  def __init__(self, arg):
    super(oo, self).__init__()
    self.arg = arg

class ClassName(object):
  """docstring for ClassName"""
  def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg
    