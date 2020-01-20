from django.db import models

class member1(models.Model): 
    objects = models.Manager() # vs code 오류 제거용

    id        = models.CharField(primary_key=True, max_length=200) 
    pw        = models.CharField(max_length=200)
    name        = models.CharField(max_length=200)
   
    age     = models.IntegerField()
    gen     = models.IntegerField() # 성별 0,1
    regdate = models.DateTimeField(auto_now_add=True) 
