from django.db import models

# Create your models here.

class Blog(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=30)

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    text = models.TextField()
    author = models.CharField(max_length=30)

