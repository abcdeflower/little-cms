from django.shortcuts import render_to_response,get_object_or_404
from django.db.models import Q
from cms.models import Story,Category
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
	template_name='cms/story_list.html'
	context_object_name='story_list'
	print('in IndexView')
	def get_queryset(self):
		print(Story.objects.all())
		return Story.objects.all()

class DetailView(generic.DetailView):
	model=Story
	template_name='cms/story_detail.html'
	def get_queryset(self):
		return Story.objects.all()

def category(request,slug):
	categpry=get_object_or_404(Category,slug=slug)
	story_list=Story.objects.filter(category=category)
	heading='分类：%s'%category.label
	return render_to_response('cms/story_list.html',locals())

def search(request):
	if 'q' in request.GET:
		term=request.GET['q'].strip()
		story_list=Story.objects.filter(Q(title__contains=term)|Q(markdown_content__contains=term))
		heading='搜索结果'
	return render_to_response('cms/story_list.html',locals())
