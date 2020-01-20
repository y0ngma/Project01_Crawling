from django.db import models

# Create your models here.
class board1(models.Model):
    objects = models.Manager()#vs code 오류 제거용

    no     = models.AutoField(primary_key = True)#게시판 글 = 기본키 
    gene   = models.CharField(max_length=200)#글 제목

    rank = models.IntegerField()
    word = models.CharField(max_length=200)

    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    time = models.IntegerField()