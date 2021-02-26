from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    carNumber=models.CharField(max_length=200,null=False,unique=True)
    CIN=models.CharField(max_length=8)
    phone= models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
 

 
 