from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Social_media_user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=250)
    address = models.TextField()
    is_moderator = models.BooleanField(default = True)


class Moderator(models.Model):
    social_media_user = models.ForeignKey(Social_media_user,on_delete=models.CASCADE)
    


