from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    description = models.CharField(max_length=300)
    Image = models.CharField(max_length=1000)


