from django.db import models

# Create your models here.

class request(models.Model): 
    land_owner=models.CharField(max_length=200,null=True)#땅 소유자 (Foreinkey)
    land_user=models.CharField(max_length=200,null=True)#땅 이용자 (Foreinkey)
    land=models.CharField(max_length=200,null=True)# 땅 (Foreinkey)
    request_condtion=models.CharField(max_length=200,null=True)#신청 현황
