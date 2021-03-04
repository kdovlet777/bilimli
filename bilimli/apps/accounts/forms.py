from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

cities = (
	('Daşoguz','Daşoguz'),
	('Lebap','Lebap'),
	('Mary','Mary'),
	('Ahal','Ahal'),
	('Balkan','Balkan'),
)
classes = (
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
	('9','9'),
	('10','10'),
	('11','11'),
)
class UserRegisterForm(UserCreationForm):
	full_name = forms.CharField(max_length = 50)
	city = forms.ChoiceField(choices = cities)
	klass = forms.ChoiceField(choices = classes)
	school = forms.IntegerField()
	class Meta:
		model = User
		fields = ['username','full_name','city','school','klass','password1',]

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ()

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('full_name','welayat','school','clasy',)