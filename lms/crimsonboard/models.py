from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class student(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
#   user_id = models.CharField(max_length=255)