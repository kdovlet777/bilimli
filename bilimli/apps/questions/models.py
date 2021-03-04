from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.utils import timezone
class Question(models.Model):
	title = models.CharField('Title', max_length = 50)
	text = models.TextField('Text')
	preview = models.CharField('Preview', max_length = 50, blank = True, null = True)
	pub_date = models.DateTimeField('Publiced Date',default = timezone.now())
	solved = models.BooleanField('solved', default = False)
	solver = models.ForeignKey(User,blank = True, null = True, on_delete = models.SET_NULL)
	comnum = models.IntegerField('Comment number',default = 0)
	answer1 = models.CharField('Answer', max_length = 50)
	actual = models.IntegerField('How many correct answers', default = 0)

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 2))
	def __str__(self):
		return self.title

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	text = models.TextField('Comment text')
	pub_date = models.DateTimeField('Comment pubdate', default = timezone.now())
	correct = models.BooleanField('Correct', default = False)

	def __str__(self):
		return self.user.username