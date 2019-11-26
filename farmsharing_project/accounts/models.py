from django.db import models
from django.contrib.auth.models import AbstractUser
from django_fields import DefaultStaticImageField

# Create your models here.

class Profile(AbstractUser):
    nickname = models.CharField(max_length = 200, null=True)#  - nickname
    sns_id = models.CharField(max_length = 200, null =True)#   - SNS_ID
    introduce = models.TextField(null=True)#   - 자기소개란
    score = models.IntegerField(null = True)#   - score
    profile_img = DefaultStaticImageField(upload_to='profile_img/', blank=True, default_image_path='images/default_profile_img.png')
    
    def __str__(self):
         return self.username


class Comment(models.Model):
    belong_to_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_comment') #유저 마이페이지에 연결
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='writer_comment') #작성자 onetoMany 관계
    comments = models.TextField(null=False) #댓글내용
    rating = models.IntegerField(null=True) #별점

class Land(models.Model): #땅
    region = models.CharField(max_length=200,null=True) #지역
    land_area = models.CharField(max_length=100,null=True) #면적
    land_condition = models.CharField(max_length=200,null=True) #땅상태
    owner_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='user_land')
    def __str__(self):
        return self.region