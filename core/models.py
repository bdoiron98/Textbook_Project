from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    major = models.ManyToManyField(Major)
    university = models.ManyToManyField(University)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.title
