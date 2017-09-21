from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^api/v1/user/register/$', views.register_user, name='registration'),
	url(r'^api/v1/user/get/(?P<id>\d*)/$', views.get_user, name='get_user'),
    # url(r'^api/create/$', create),
    # url(r'^api/update/(?P<id>\d*)$', update),
    # url(r'^api/delete/(?P<id>\d*)$', delete),
]