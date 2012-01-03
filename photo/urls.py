from django.conf.urls.defaults import *
from mysite.photo.models import Item, Photo

urlpatterns = patterns('django.views.generic',
    url(r'^$', 'simple.direct_to_template',
    kwargs = {
        'template':'index.html',
        'extra_context':{'item_list':lambda:Item.objects.all()}
    },
    name='index'
    ),
    url(r'^items/$', 'list_detail.object_list',
    kwargs={
        'queryset':Item.objects.all(),
        'template_name':'items_list.html',
        'allow_empty':True
    },
    name = 'item_list'
    ),
    
    )