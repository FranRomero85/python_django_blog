from django.conf.urls import *
from blog.views import index,archive

urlpatterns=patterns('',
            url(r'^$',index),
            url(r'^(?P<blog_id>\d+)/$',archive)
             )