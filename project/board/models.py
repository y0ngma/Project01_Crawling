from django.db import models

class Table1(models.Model):
    objects = models.Manager() # vs code 오류 제거용

    no    = models.AutoField(primary_key=True) # 자동 번호매기기
    age   = models.CharField(max_length=200)
    rank  = models.CharField(max_length=200)
    word  = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    day   = models.CharField(max_length=200)
    time  = models.CharField(max_length=200)
    
    # rank = models.TextField()
    # word  = models.CharField(max_field=50)
    # month = models.DateTimeField(auto_now_add=True)
    # day = models.DateTimeField(auto_now_add=True)
    # time = models.DateTimeField(auto_now_add=True)