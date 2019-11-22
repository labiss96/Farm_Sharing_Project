from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):
    nickname = models.CharField(max_length = 200, null=True)#  - nickname
    email = models.CharField(max_length = 200, null =True, unique=True)#   - email
    sns_id = models.CharField(max_length = 200, null =True)#   - SNS_ID
    introduce = models.TextField(null=True)#   - 자기소개란
    #   - 땅(Foreignkey)
    score = models.IntegerField(null = True)#   - score

    def __str__(self):
         return self.username