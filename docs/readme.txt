Python.Web.Development.with.Django
==================================

2012.01.03
----------

   1. p147

   2. xml to python data
   http://code.activestate.com/recipes/534109-xml-to-python-data-structure/
   utils/xml2obj.py
   
   ipython
import utils
>>> SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
... <address_book>
...   <person gender='m'>
...     <name>fred</name>
...     <phone type='home'>54321</phone>
...     <phone type='cell'>12345</phone>
...     <note>&quot;A<!-- comment --><![CDATA[ <note>]]>&quot;</note>
...   </person>
... </address_book>
... """
>>> address_book = xml2obj(SAMPLE_XML)
>>> person = address_book.person   

   有问题，没成功

   3. xml writer

from utils import xmlWriter

doc = xmlWriter.XmlWriter()
node = doc.createNode('node1', withAttribs = {'1': 'first', '2': 'second'})
node2 = doc.createNode('node2', node, withAttribs = {'3': 'third'})
node3 = doc.createNode('node3', node, withAttribs = {'4': 'fourth'})
doc.printXML()

   4. 另一个例子
   manage.py startapp photo
        

   5. 注意python 文件中tab,whitespace 问题，不要混用，建议设置tab为4位空格
      
      简明python编程风格save/python.style.txt

   6. photo

   TODO
   index.html extend base.html ,会自动用blog的base.html

   图片能上载到指定目录，但不能正常显示

   7. cms 
   p206

2011.12.31
----------

   1. 

   manage shell
   raise AlreadyRegistered('The model %s is already registered' % model.__name__)
   
   manage.py dumpdata --indent=4 blog>blog.json
   
2011.12.30
----------

   1. py 文件运行
   save/*.reg

   2. p133

2011.12.28
----------

   1. p124
   
2011.12.26
-----------

   1. p116

2011.12.25
-----------

   1. p100
   
   2. 

   --create new repos
   https://github.com/repositories/new

   git remote add origin git@github.com:yangjiandong/mysite.git
   git push origin master
   
2011.12.24
-----------

   1. django-admin startproject mysite

   cd mysite
   manage.py runserver

   manage.py startapp blog

   --create tables, and every add app to INSTALLED_APPS IN setting.py
   manage.py syncdb

   p92
   
   --END