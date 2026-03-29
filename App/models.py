from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

# Advisor details

class TEACHER(models.Model):
    Advisor=models.ForeignKey(User,on_delete=models.CASCADE)
    TEACHER_NAME=models.CharField(max_length=30,null=True)
    TEACHER_PHONE=models.CharField(max_length=10)
    TEACHER_DEPT=models.CharField(max_length=30,null=True)

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
#barcode reader

class Details_students(models.Model):
    TEACHER_NAME=models.ForeignKey(TEACHER,on_delete=models.CASCADE) 
    ADMISSION_NO=models.CharField(max_length=20, unique=True)
    NAME=models.CharField(max_length=100)
    DEPARTMENT= models.CharField(max_length=50)
    BRANCH=models.CharField(max_length=20)
    YEAR=models.CharField(max_length=20)
    PHONE1= models.CharField(max_length=10)
    PHONE2 = models.CharField(max_length=10, blank=True, null=True)

#Gate pass
    
class Gate_Pass(models.Model):
    STUD_NAME=models.CharField(max_length=20)  
    STUD_BRANCH=models.CharField(max_length=20)
    STUD_YEAR=models.CharField(max_length=20)
    STUD_PHONE1= models.CharField(max_length=10)
    APPORVED=models.CharField(max_length=50)
    REASONS=models.CharField(max_length=50)
    TEACHER_ID=models.ForeignKey(TEACHER,on_delete=models.CASCADE)
    STUDENT_ID=models.ForeignKey(Details_students,on_delete=models.CASCADE)
    HOD_APPROVE=models.CharField(max_length=50,default="NO")
    gate_date = models.DateField(auto_now_add=True)
    gate_time = models.TimeField(auto_now_add=True)
    exit_time=models.TimeField(null=True, blank=True)
    re_enrty_time=models.TimeField(null=True, blank=True)

# class Security_Gate(models.Model):
#     TEACHER_ID=models.ForeignKey(TEACHER,on_delete=models.CASCADE)
#     STUDENT_ID=models.ForeignKey(Details_students,on_delete=models.CASCADE)
#     GATE_PASS=models.ForeignKey(Gate_Pass,on_delete=models.CASCADE)
#     GATE_STUD_NAME=models.CharField(max_length=20)  
#     GATE_STUD_BRANCH=models.CharField(max_length=20)
#     GATE_STUD_YEAR=models.CharField(max_length=20)
#     gate_time = models.TimeField()
#     re_entry= models.TimeField()


    
    
