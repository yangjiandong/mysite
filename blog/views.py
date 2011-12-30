# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mysite.blog.models import BlogPost

def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))
	
from mysite.blog.models import Book
from datetime import datetime
from somewhere import some_function_returing_a_queryset

def q(request):
	book_queryset = some_function_returing_a_queryset()
	today = datetime.now()
	overdue_books = book_queryset.filter(due_date__lt=today)	