from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class BlogPost(TimeStampedModel):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    post = models.TextField()

