# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('post.Post')

    def __unicode__(self):
        return self.text[:20]
