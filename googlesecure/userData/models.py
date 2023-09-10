from django.db import models

# Create your models here.
class UserData(models.Model):
    email=models.TextField(max_length=300)
    pswd=models.TextField(max_length=300)

class UserEmail(models.Model):
    email=models.TextField(max_length=300,null=True)

class UserPswd(models.Model):
    pswd=models.TextField(max_length=300,null=True)