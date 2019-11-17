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
