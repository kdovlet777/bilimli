from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user','text']
admin.site.register(Comment,CommentAdmin)