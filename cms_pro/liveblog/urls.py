from django.conf.urls import include,url
from liveblog import views

urlpatterns=[
	url(r'^$',views.IndexView.as_view(),name='blog-index'),
	url(r'^updates-after/(?P<id>\d+)/$',views.updates_after,name='updates_after'),
	#url(r'^(?P<path>.*)','django.views.static.serve'),
	]
