from django.db import models
from django.contrib.auth import get_user_model


# class Author(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
# class Major(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
# class University(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=2)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.title
