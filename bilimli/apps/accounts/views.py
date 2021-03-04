from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            new_user = form.save(commit=False)
            new_user.save()
            profile = Profile.objects.create(user = new_user)
            profile.full_name = form.cleaned_data.get('full_name')
            profile.welayat = form.cleaned_data.get('city')
            profile.clasy = form.cleaned_data.get('klass')
            profile.save()
            messages.success(request, f'Account created for {username}. Now you can login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def edit(request):
    top_users = Profile.objects.order_by('-rating')[:10]
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data = request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('questions:index')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'accounts/edit.html', {'user_form':user_form, 'profile_form': profile_form, 'top_users':top_users})

@login_required
def profile(request, username):
    top_users = Profile.objects.order_by('-rating')[:10]
    user1 = User.objects.get(username = username)
    return render(request, 'accounts/profile.html', {'user1':user1, 'top_users':top_users})