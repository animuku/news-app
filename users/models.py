from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sources = models.CharField(max_length=10000,null=True)
    image = models.ImageField(default = 'default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username+"Profile"