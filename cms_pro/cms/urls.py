from django.conf.urls import url
from cms import views

urlpatterns=[
	url(r'^(?P<slug>[-\w]+)/$',views.DetailView.as_view(),name='cms-story'),
	url(r'^$',views.IndexView.as_view(),name='cms-home'),
	url(r'^category/(?P<slug>[-\w]+)/$',views.category,name='cms-category'),
	]
