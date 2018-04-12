from django.db import models
import datetime

# Create your models here.
class Update(models.Model):
	timestamp=models.DateTimeField(default=datetime.datetime.now)
	text=models.TextField()
	
	class Meta:
		ordering=['-id']

	def __str__(self):
		return "[%s] %s"%(self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),self.text)


