from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

# Advisor details

class TEACHER(models.Model):
    Advisor=models.ForeignKey(User,on_delete=models.CASCADE)
    TEACHER_NAME=models.CharField(max_length=30,null=True)
    TEACHER_PHONE=models.CharField(max_length=10)

# Hod details

class HOD(models.Model):
    HOD=models.ForeignKey(User,on_delete=models.CASCADE)
    TEACHER_NAME=models.CharField(max_length=30,null=True)
    TEACHER_PHONE=models.CharField(max_length=10)

# Security details

class Security(models.Model):
    SECURITYY=models.ForeignKey(User,on_delete=models.CASCADE)
    SECURITY_NAME=models.CharField(max_length=30,null=True)
    SECURITY_PHONE=models.CharField(max_length=10)
