from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User_model(AbstractUser):
    is_user = models.BooleanField(default = 0)
    is_moderator = models.BooleanField(default = 0)





