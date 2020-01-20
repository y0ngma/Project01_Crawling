from django.db import models

class board1(models.Model):
    objects = models.Manager() # vs code 오류 제거용

    no    = models.AutoField(primary_key=True) # 자동 번호매기기
    gene  = models.CharField(max_length=200) #generation 글자
    
    rank  = models.IntegerField() # 순위는 숫자
    word  = models.CharField(max_length=200)
    
    year  = models.IntegerField()
    month = models.IntegerField()
    day   = models.IntegerField()
    time  = models.IntegerField()
    