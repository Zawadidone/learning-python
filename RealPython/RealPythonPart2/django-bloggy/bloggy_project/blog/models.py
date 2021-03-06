# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from uuslug import uuslug


# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
