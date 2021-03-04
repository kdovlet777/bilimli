from django.urls import path

from .views import register, edit, profile
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', register, name='register'),
    path('login/', auth_views.LoginView
         .as_view(template_name='register/login.html'), name='login'),
    path('edit/',edit, name='edit'),
    path('profile/<username>', profile, name='profile')
]
