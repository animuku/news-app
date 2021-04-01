from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=1000,primary_key=True)
    date_posted = models.DateField(default=timezone.now)
    source = models.CharField(max_length=100,default="NA")
    url_to_image = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return self.title