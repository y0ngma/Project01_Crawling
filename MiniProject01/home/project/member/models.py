from django.db import models

# Create your models here.
class member1(models.Model):
    object = models.Manager()#vs code 오류 제거용
    id     = models.CharField(primary_key = True, max_length=200)#게시판 글 = 기본키 
    pw   = models.CharField(max_length=200)#글 제목
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gen = models.IntegerField()
    joindate = models.DateField(auto_now_add=True)