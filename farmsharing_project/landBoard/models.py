from django.db import models
from polymorphic.models import PolymorphicModel

# Abstract class
class LandBoard(PolymorphicModel):
    title = models.CharField(max_length=100) #제목
    region = models.CharField(max_length=100) #지역
    land_area = models.FloatField() #면적
    sharing_term = models.CharField(max_length=100) #공유기간
    is_free = models.BooleanField() #무료여부
    amount = models.IntegerField() #금액
    # writer = models.ForeignKey(Profile)#작성자
    content = models.TextField() #글 내용
    recruitment_status = models.CharField(max_length=30) #모집현황

    def __str__(self):
        return self.name

# 땅 소유자가 올리는 공유게시판
class SharingBoard(LandBoard): 
    land_img = models.CharField(max_length=100) #땅 사진 -> 나중에 image필드로 바꿀 것.

# 땅 요청자가 올리는 요청게시판
class RequestBoard(LandBoard): 
    purpose = models.CharField(max_length=100) #사용 목적