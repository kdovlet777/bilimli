from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from accounts.models import Profile
from django.core.paginator import Paginator

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')
	top_users = Profile.objects.order_by('-rating')[:10]
	for a in latest_articles_list:
		a.preview = a.text[:30] + '...'
		a.save()
	paginator = Paginator(latest_articles_list, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	count_pages = int(page_obj.paginator.num_pages)
	pages = [int(i) for i in range(1,count_pages+1)]
	return render(request, 'articles/list.html',{'latest_articles_list':latest_articles_list,'page_obj':page_obj, 'pages':pages, 'top_users':top_users})

def detail(request, article_id):
	a = Article.objects.get(id = article_id)
	top_users = Profile.objects.order_by('-rating')[:10]
	comment_list = a.comment_set.order_by('-pub_date')
	return render(request, 'articles/detail.html',{'a':a, 'comment_list':comment_list, 'top_users':top_users})

def leave_comment(request, article_id):
	a = Article.objects.get(id = article_id)
	a.comment_set.create(user = request.user, text = request.POST['text'])
	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))