from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32)
    text = models.CharField(max_length=1024)
