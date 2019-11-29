from django.db import models
from accounts.models import *

class QuestionBoard(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date published',null=True)#글 게시 날짜
    body = models.TextField()

    def __str__(self):
        return self.title 

class QB_comment(models.Model):
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_content = models.TextField()
    qbcomment = models.ForeignKey(QuestionBoard, on_delete=models.CASCADE)

class DealBoard(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField('Date published',null=True)#글 게시 날짜
    prod_img = DefaultStaticImageField(upload_to='prod_img/', blank=True, default_image_path='images/default_profile_img.png')
    like=models.ManyToManyField(Profile, blank=True,related_name="Deal_like")
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def total_likes(self):
        return self.like.count()

class DB_comment(models.Model):
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_content = models.TextField()
    dbcomment = models.ForeignKey(DealBoard, on_delete=models.CASCADE)
