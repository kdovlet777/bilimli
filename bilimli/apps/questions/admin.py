from django.contrib import admin
from .models import Question, Answer
class QuestionAdmin(admin.ModelAdmin):
	list_display = ['title','preview', 'solved','solver']
admin.site.register(Question,QuestionAdmin)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user','text','pub_date']
admin.site.register(Answer, CommentAdmin)