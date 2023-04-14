from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=64)
    user_password = models.CharField(max_length=64)
