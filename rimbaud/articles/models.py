from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    article = models.TextField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    visibility = models.BooleanField()
