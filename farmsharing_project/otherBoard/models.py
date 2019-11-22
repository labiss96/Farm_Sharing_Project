from django.db import models

# Create your models here.
class Successful_case_board(models.Model): #성공 사례 게시판
    title=models.CharField(max_length=200,null=True)
    writer=models.CharField(max_length=200,null=True)
    body=models.CharField(max_length=200,null=True)
    picture=models.CharField(max_length=200,null=True) # 이단은 타입은 string임
    score=models.IntegerField(default=0) #별점

class Team_recruitment_board(models.Model): #팀 모집 게시판
    title=models.CharField(max_length=200,null=True)
    region=models.CharField(max_length=200,null=True)#지역
    recruitment_number=models.IntegerField(default=0)#모집 인원
    current_recruitment_condition=models.CharField(max_length=200,null=True) #모집현황
    active_period=models.IntegerField(default=0)#활동 기간
    purpose=models.CharField(max_length=200,null=True)#사용 목적
    body=models.CharField(max_length=200,null=True) #내용
    
