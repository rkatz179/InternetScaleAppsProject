from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^api/get/$', getItemList),
    url(r'^api/get/(?P<id>\d*)$', getItem),
    url(r'^api/create/$', create),
    url(r'^api/update/(?P<id>\d*)$', update),
    url(r'^api/delete/(?P<id>\d*)$', delete),

]