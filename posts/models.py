from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    body = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='N/A')
    author = models.CharField(max_length=255, default='N/A')
    new = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.title
