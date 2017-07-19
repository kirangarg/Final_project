# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=255)
    verified_phone =  models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)


