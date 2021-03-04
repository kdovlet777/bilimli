from django.urls import path

from . import views
app_name = 'questions'
urlpatterns = [
	path('',views.index,name='index'),
	path('<int:question_id>', views.detail, name = 'detail'),
	path('<int:question_id>/leave_answer', views.leave_answer, name = 'leave_answer'),
]
