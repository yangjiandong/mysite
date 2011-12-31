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
#from somewhere import some_function_returing_a_queryset
from django.db.models import Q

def q(request):
	book_queryset = some_function_returing_a_queryset()
	today = datetime.now()
	overdue_books = book_queryset.filter(due_date__lt=today)
	
	#Q
	specific_does = Person.objects.filter(last="Doe").exclude(
		Q(first="John") | Q(middle="Quincy")
	)
	
	# grabs all the Does, named John Smith,but not any one named John W.Smith
	other_does = Person.objects.filter(Q(last="Doe") | 
		(Q(last="Smith") & Q(first="John") & ~Q(middle__startswith="W"))
		)

from django.db import connection

def queryo():
	cursor = connection.cursor()
	cursor.execute("select * from blog_person")
	doe_rows = cursor.fetchall()
	for row in doe_rows:
		print "%S %s" % (row[0], row[1])