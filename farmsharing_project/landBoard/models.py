from django.db import models
from polymorphic.models import PolymorphicModel

class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region


# Abstract class
class LandBoard(PolymorphicModel):
    title = models.CharField(max_length=100) #제목
    # REGION_CHOICE= (
    #     ('서울','서울'),
    #     ('부산','부산'),
    #     ('대구','대구'),
    #     ('인천','인천'),
    #     ('광주','광주'),
    #     ('대전','대전'),
    #     ('울산','울산'),
    #     ('세종','세종'),
    #     ('경기','경기'),
    #     ('강원','강원'),
    #     ('충북','충북'),
    #     ('충남','충남'),
    #     ('전북','전북'),
    #     ('전남','전남'),
    #     ('경북','경북'),
    #     ('경남','경남'),
    #     ('제주','제주'),
    # ) # jongmin 이 추가한 튜플
    region = models.CharField(max_length=100) #지역
    land_area = models.FloatField() #면적
    # TERM_CHOICE =(
    #     ('하루','하루'),
    #     ('일주일 이내','일주일 이내'),
    #     ('1년','1년'),
    #     ('3년','3년'),
    #     ('5년','5년'),
    # ) # jongmin 이 추가한 튜플
    sharing_term = models.CharField(max_length=100) #공유기간
    is_free = models.CharField(max_length=100) #무료여부
    amount = models.IntegerField() #금액
    # writer = models.ForeignKey(Profile)#작성자
    content = models.TextField() #글 내용
    # STATUS_CHOICE=(
    #     ('모집중','모집중'),
    #     ('모집마감','모집마감'),
    # )
    recruitment_status = models.CharField(max_length=30) #모집현황

    def __str__(self):
        return self.title

# 땅 소유자가 올리는 공유게시판
class SharingBoard(LandBoard): 
    land_img = models.ImageField() #땅 사진 -> 나중에 image필드로 바꿀 것.
    
# 땅 요청자가 올리는 요청게시판
class RequestBoard(LandBoard): 
    purpose = models.CharField(max_length=100) #사용 목적