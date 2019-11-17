# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UpdateUserForm, UpdateUserProfileForm, PostForm, CommentForm, UserRegistrationForm
from .models import Post, Profile


from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
        params = {
            'form': form
        }
    return render(request, 'registration/register.html', locals())


@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    users = User.objects.all()
    posts = Post.get_all_posts()
    print(posts)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
        params = {
        'images': images,
        'form': form,
        'users': users,
        'posts': posts,
    }
    return render(request, 'insta/index.html', locals())


@login_required(login_url='login')
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
        print(images)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,
 