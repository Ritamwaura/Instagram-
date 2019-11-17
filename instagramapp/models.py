# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="Users biography", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    
    class Meta:
        db_table = 'profile'

    def __str__(self):
        return f'{self.user.username} : {self.location}'    

@receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
class Post(models.Model):
        image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    
    class Meta:
        db_table = 'posts'

    @property
    def get_all_comments(self):
        return self.comments.all()
    
     @property
    def save_image(self):
        self.save()

    @classmethod
    def get_all_posts(cls):
        return cls.objects.all()
    @property
    def delete(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.name} Post'

