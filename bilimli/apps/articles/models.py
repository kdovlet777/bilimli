from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.utils import timezone

class Article(models.Model):
	title = models.CharField('Title', max_length = 100)
	text = models.TextField('Text')
	preview = models.CharField('Preview', max_length = 100)
	pub_date = models.DateTimeField('Publiced Date', auto_now_add = True)
	image = models.ImageField('Image', blank=True, null = True, upload_to = 'media')
	
	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Comment')
	text = models.TextField('Text')
	pub_date = models.DateTimeField('Publiced Date',auto_now_add = True)

	def __str__(self):
		return self.user.username