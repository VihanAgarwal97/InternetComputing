from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
	text = models.TextField()
	sent = models.BooleanField()
	date = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey('auth.User', related_name="author_msgs")
	receiver = models.ForeignKey('auth.User', related_name = "receiver_msgs")