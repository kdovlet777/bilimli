from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Answer
from accounts.models import Profile
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

def index(request):
	questions = Question.objects.order_by('-id')
	top_users = Profile.objects.order_by('-rating')[:10]
	for question in questions:
		question.preview = question.text[:45] + '...'
		question.comnum = question.answer_set.count()
	question.save()
	paginator = Paginator(questions, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	count_pages = int(page_obj.paginator.num_pages)
	pages = [int(i) for i in range(1,count_pages+1)]
	return render(request, 'questions/list.html',{'questions':questions, 'top_users':top_users, 'page_obj':page_obj, 'pages':pages})

def detail(request, question_id):
	a = Question.objects.get(id = question_id)
	top_users = Profile.objects.order_by('-rating')[:10]
	answer_list = a.answer_set.order_by('-pub_date')[:10:-1]
	for answer in a.answer_set.all():
		if answer.text == a.answer1 and a.solved == False:
			answer.correct = True
		if answer.correct and a.solved == False:
			answer.user.profile.rating += a.actual
			a.solved = True
			a.solver = answer.user 
		answer.save()
		a.comnum = a.answer_set.count()
		a.save()
		answer.user.profile.save()
	return render(request, 'questions/detail.html',{'answer_list':answer_list, 'q':a,'top_users':top_users})

def leave_answer(request, question_id):
	a = Question.objects.get(id = question_id)
	a.answer_set.create(user = request.user, text = request.POST['text'])
	return HttpResponseRedirect( reverse('questions:detail', args = (a.id,)))