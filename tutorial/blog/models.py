from django.db import models

# Create your models here.

class Blog(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    text = models.TextField()
    author = models.CharField(max_length=30)

