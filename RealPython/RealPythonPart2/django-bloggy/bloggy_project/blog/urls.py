from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_post/$', views.add_post, name='add_post'),  # add post form
    url(r'^(?P<title>[-\w]+)/$',	views.post,	name='post'),
    url(r'^delete_post/(?P<title>[\w-]+)/$', views.delete_post, name='delete_post'),
]
