from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Reviews(models.Model):
    # rating          = models.
    title           = models.CharField(max_length=64)
    body            = models.TextField(max_length=10000)
    ipAddress       = models.GenericIPAddressField(blank=True, null=True)
    submitted_on    = models.DateTimeField(default=datetime.now)
    company         = models.CharField(max_length = 200, blank=False)
    reviewer_Email  = models.EmailField(max_length=250)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Reviews"

class Login(models.Model):
    User_Name       = User()
    Password        = models.CharField(max_length=30)
    