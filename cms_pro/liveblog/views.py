from django.http import HttpResponse
from django.core import serializers
from django.views import generic

from liveblog.models import Update

def updates_after(request,id):
	response=HttpResponse()
	response['Content-Type']="text/javascript"
	response.write(serializers.serialize("json",Update.objects.filter(pk__gt=id)))

class IndexView(generic.ListView):
	template_name='liveblog/update_list.html'
	def get_queryset(self):
		return Update.objects.all()
