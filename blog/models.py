from django.db import models
from django.utils import timezone
import datetime


class Blog(models.Model):
	title = models.CharField(max_length = 100)
	text = models.TextField()
	pub_date = models.DateTimeField(default = timezone.now())
	def __str__(self):
		return self.title
	
class Author(models.Model):
	name=models.CharField(max_length=100)
	email = models.EmailField()
	blog = models.ManyToManyField(Blog)
	def __str__(self):
		return self.name
	