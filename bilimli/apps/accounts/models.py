from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	full_name = models.CharField('Full name', max_length=50, null = True, blank = True)
	welayat = models.CharField('Which welayat', null = True, blank = True,max_length=15)
	school = models.IntegerField('School №',default = 0)
	clasy = models.IntegerField('Class',null = True, blank = True)
	rating = models.IntegerField('Rating', default = 0)
	def __unicode__(self):
		return u'Profile of user: %s' % self.user.username