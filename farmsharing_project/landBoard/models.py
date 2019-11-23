from django.db import models
from polymorphic.models import PolymorphicModel
from accounts.models import *

class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region


# Abstract class
class LandBoard(PolymorphicModel):
    title = models.CharField(max_length=100) #제목
    region = models.CharField(max_length=100) #지역
    land_area = models.FloatField() #면적
    sharing_term = models.CharField(max_length=100) #공유기간
    is_free = models.CharField(max_length=100) #무료여부
    amount = models.IntegerField() #금액
    content = models.TextField() #글 내용
    recruitment_status = models.CharField(max_length=30) #모집현황

    def __str__(self):
        return self.title

# 땅 소유자가 올리는 공유게시판
class SharingBoard(LandBoard): 
    land_img = models.ImageField() #땅 사진 -> 나중에 image필드로 바꿀 것.
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_sb') #작성자 - 땅게시판 (1:N) 관계설정.
    choice_land = models.ForeignKey(Land, on_delete=models.CASCADE)
# 땅 요청자가 올리는 요청게시판
class RequestBoard(LandBoard): 
    purpose = models.CharField(max_length=100) #사용 목적
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_rb') #작성자 - 땅게시판 (1:N) 관계설정.

class SB_comment(models.Model):
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_content = models.TextField()
    sbcomment = models.ForeignKey(SharingBoard, on_delete=models.CASCADE)

class RB_comment(models.Model):
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_content = models.TextField()
    land_writer = models.ForeignKey(Land,on_delete=models.CASCADE)
    rbcomment = models.ForeignKey(RequestBoard, on_delete=models.CASCADE)