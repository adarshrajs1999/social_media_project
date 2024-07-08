from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User_model(AbstractUser):
    is_user = models.BooleanField(default = 0)
    is_moderator = models.BooleanField(default = 0)

class Social_media_user(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 250)
    email = models.EmailField()
    bio = models.TextField()
    address = models.TextField()
    profile_picture = models.ImageField(upload_to = 'myfiles')


class Moderator(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 250)
    email = models.EmailField()
    bio = models.TextField()
    address = models.TextField()
    profile_picture = models.ImageField(upload_to = 'myfiles')

