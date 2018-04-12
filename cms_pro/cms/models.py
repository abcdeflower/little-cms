from django.db import models
from markdown import markdown
import datetime
from django.db.models import permalink
from django.contrib.auth.models import User
# Create your models here.

VIEWABLE_STATUS=[3,4]

class ViewwableManager(models.Manager):
	def get_queryset(self):
		default_queryset=super(ViewwableManager,self).get_queryset()
		return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Category(models.Model):
	label=models.CharField(blank=True,max_length=50)
	slug=models.SlugField()

	class Meta:
		verbose_name_plural='categories'

	def __str__(self):
		return self.label

class Story(models.Model):
	STATUS_CHOICES=(
	(1,'待编辑'),
	(2,'待审核'),
	(3,'发布'),
	(4,'存档'),
	)
	
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	markdown_content=models.TextField()
	html_content=models.TextField(editable=False)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	status=models.IntegerField(choices=STATUS_CHOICES,default=1)
	created=models.DateTimeField(default=datetime.datetime.now)
	modified=models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		ordering=['modified']
		verbose_name_plural='stories'
	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('cms-story',(),{'slug':self.slug})
	def save(self):
		self.html_content=markdown(self.markdown_content)
		self.modified=datetime.datetime.now()
		super(Story,self).save()
	admin_objects=models.Manager()
	objects=ViewwableManager()
