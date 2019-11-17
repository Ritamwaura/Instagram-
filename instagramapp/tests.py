# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.test import TestCase

# Create your tests here.

new_post = Post(image='default.jpg', name='brn', caption='the best house', likes='', user=Profile.user)
new_profile = Profile(user=new_post.user, profile_pic='default.jpg', bio='my user bio', name='Rita', location='nairobi')


class TestProfile(TestCase):
    def setUp(self) -> None:
        self.new_profile = Profile(user=new_post.user, profile_pic='default.jpg', bio='my user bio', name='Rita',
                                   location='nairobi')

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_user(self):
        before = Profile.objects.count()
        self.new_profile.save_location()
        after = Profile.objects.count()
        self.assertTrue(before < after)

    def test_delete_user(self):
        before = Profile.objects.count()
        self.new_profile.save_location()
        after = Profile.objects.count()
        self.assertTrue(before > after)

    def tearDown(self) -> None:
        self.new_profile.delete()


class TestPost(TestCase):
    def setUp(self) -> None:
        self.new_post = Post(image='default.jpg', name='brn', caption='the best house', likes='', user=Profile.user)

    def test_post_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_all_comments(self):
        self.assertTrue(len(Post) > 0)

    def test_save_image(self):
        before = Post.objects.count()
        self.new_post.save_location()
        after = Post.objects.count()
        self.assertTrue(before < after)

    def test_delete_image(self):
        before = Post.objects.count()
        self.new_post.save_location()
        after = Post.objects.count()
        self.assertTrue(before > after)

    def tearDown(self) -> None:
        self.new_post.delete()

