from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='images/')
