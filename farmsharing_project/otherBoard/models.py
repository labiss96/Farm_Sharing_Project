from django.db import models
from accounts.models import *

# Create your models here.
class Review(models.Model): #성공 사례 게시판
    title=models.CharField(max_length=200,null=True)
    writer=models.ForeignKey(Profile, on_delete = models.CASCADE)
    body=models.CharField(max_length=200,null=True)
    picture=DefaultStaticImageField(upload_to='picture/', blank=True, default_image_path='images/default_profile_img.png') # 이단은 타입은 string임
    score=models.IntegerField(default=0) #별점
    pub_date = models.DateTimeField('Date published',null=True)#글 게시 날짜
    like=models.ManyToManyField(Profile, blank=True,related_name="Profile_like")

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.like.count()

class Join(models.Model): #팀 모집 게시판
    title=models.CharField(max_length=200,null=True)
    writer=models.ForeignKey(Profile, on_delete = models.CASCADE)
    region=models.CharField(max_length=200,null=True)#지역
    joined_people=models.IntegerField(default=0)#모집 인원
    current_joined=models.BooleanField(max_length=200, default = True) #모집현황
    active_period_start=models.CharField(max_length = 200,default=0)#활동 기간 시작
    active_period_end=models.CharField(max_length = 200,default=0)#활동 기간 끝
    purpose=models.CharField(max_length=200,null=True)#사용 목적
    body=models.CharField(max_length=200,null=True) #내용
    pub_date = models.DateTimeField('Date published',null=True)#글 게시 날짜
    scrap=models.ManyToManyField(Profile, blank=True,related_name="Profile_scrap")
    def __str__(self):
        return self.title

class Join_comments(models.Model):
    writer = models.ForeignKey(Profile, on_delete = models.CASCADE)
    content = models.TextField()
    join = models.ForeignKey(Join, on_delete = models.CASCADE)

class Review_comments(models.Model):
    writer = models.ForeignKey(Profile, on_delete = models.CASCADE)
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
  
