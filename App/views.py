from django.shortcuts import render, redirect
# connecting models
from . models import *
# connecting Athenticaton Table
from django.contrib.auth.models import User, auth
#log out
from django.contrib.auth import logout

# Create your views here.

#-----------HOMES------------------

def home(request):
    return render(request, 'Aa_main.html')
def advisor_home(request):
    return render(request, 'Advisor_home.html')
def hod_home(request):
    return render(request, 'Hod_home.html')
def security_home(request):
    return render(request, 'Security_home.html')

#-----ADVISOR LOGIN AND SIGN UP-------

#---------Sign up starting------------

def Advisor_sign(request):
     if request.method == 'POST':
        Teacher_Name = request.POST['teacher_name']
        Teacher_Id = request.POST['teacher_id']
        Teacher_Email = request.POST['teacher_email']
        Teacher_Phone = request.POST['teacher_phone']
        Pas = request.POST['pass']
        Cpas = request.POST['c_pass']
        if Pas == Cpas:
            user = None
            if User.objects.filter(username=Teacher_Id).exists():
                user = User.objects.get(username=Teacher_Id)
                if TEACHER.objects.filter(Advisor=user).exists():
                    print("username alerady exists ")
                    return render(request, 'Advisor_sign_in.html', {'key': 'username already exists'})
            else:
                User.objects.create_user(
                    username=Teacher_Id, email=Teacher_Email, password=Pas, first_name=Teacher_Name).save()
                user = User.objects.get(username=Teacher_Id)
            if user:
                if TEACHER.objects.filter(TEACHER_NAME=Teacher_Id).exists():
                    print("user alerady exists ")
                    return render(request, 'Advisor_sign_in.html', {'key': 'user already exists'})
                else:
                    TEACHER(Advisor=user, TEACHER_NAME=Teacher_Name,
                            TEACHER_PHONE=Teacher_Phone).save()
                    print('REGISTERED SUCCESSFULLY')
                    return redirect(Advisor_log)
        else:
            print('password does not match')
            return render(request, 'Advisor_sign_in.html', {'key': 'password does not match'})
     return render(request,'Advisor_sign_in.html')
   # return render(request,'Advisor_sign _in.html')

#---------Sign up ending------------

#---------login Starting------------

def Advisor_log(request):
    if request.method=='POST':
        adv_id=request.POST['Ad_id']
        advi_pass=request.POST['pass']
        if TEACHER.objects.filter(Advisor__username=adv_id).exists():
            use=auth.authenticate(username=adv_id, password=advi_pass)
            if use is not None:
             auth.login(request,use)
             print('sucess login')
             return redirect(advisor_home)
            else:
             print('invalid')
             return render(request,'Advisor_log_in.html',{'key':'INVALID USERNAME AND PASSWORD'})
        else:
             print('Not found')
             return render(request,'Advisor_log_in.html',{'key':'USERNAME NOT FOUND'})
    return render(request,'Advisor_log_in.html')

#-----------login ending--------------

#-----------HOD LOGIN/SIGN UP---------

#-----------sign up start-------------

def Hod_sign(request):
    if request.method == 'POST':
        Teacher_Name = request.POST['hod_name']
        Teacher_Id = request.POST['hod_id']
        Teacher_Email = request.POST['hod_email']
        Teacher_Phone = request.POST['hod_phone']
        Pas = request.POST['pass']
        Cpas = request.POST['c_pass']
        if Pas == Cpas:
            user = None
            if User.objects.filter(username=Teacher_Id).exists():
                user = User.objects.get(username=Teacher_Id)
                if HOD.objects.filter(HOD__username=user).exists():
                    print("username alerady exists ")
                    return render(request, 'Advisor_sign_in.html', {'key': 'username already exists'})
            else:
                User.objects.create_user(
                    username=Teacher_Id, email=Teacher_Email, password=Pas, first_name=Teacher_Name).save()
                user = User.objects.get(username=Teacher_Id)
            if user:
                if HOD.objects.filter(TEACHER_NAME=Teacher_Id).exists():
                    print("user alerady exists ")
                    return render(request, 'Hod_sign.html', {'key': 'user already exists'})
                else:
                    HOD(HOD=user, TEACHER_NAME=Teacher_Name,
                            TEACHER_PHONE=Teacher_Phone).save()
                    print('REGISTERED SUCCESSFULLY')
                    return redirect(Hod_log)
        else:
            print('password does not match')
            return render(request, 'Hod_sign.html', {'key': 'password does not match'})
    return render(request,'Hod_sign.html')

#----------------Sign up ending-------------

#-------------HOD login starting-------------

def Hod_log(request):
    if request.method=='POST':
        hod_id=request.POST['hod_id']
        hod_pass=request.POST['pass']
        if HOD.objects.filter(HOD__username=hod_id).exists():
            use=auth.authenticate(username=hod_id, password=hod_pass)
            if use is not None:
             auth.login(request,use)
             print('sucess login')
             return redirect(hod_home)
            else:
             print('invalid')
             return render(request,'HOd_log.html',{'key':'INVALID USERNAME AND PASSWORD'})
        else:
             print('Not found')
             return render(request,'HOd_log.html',{'key':'USERNAME NOT FOUND'})
    return render(request,'HOd_log.html')

#----------------login ending-------------

#-----------SECURITY LOGIN/SIGN UP--------

#--------------sign up start--------------

def security_sign(request):
    if request.method == 'POST':
        Security_Name = request.POST['security_name']
        Security_Id = request.POST['security_id']
        Security_Email = request.POST['security_email']
        Security_Phone = request.POST['security_phone']
        Pas = request.POST['pass']
        Cpas = request.POST['c_pass']
        if Pas == Cpas:
            user = None
            if User.objects.filter(username=Security_Id).exists():
                user = User.objects.get(username=Security_Id)
                if Security.objects.filter(SECURITY_NAME=user).exists():
                    print("username alerady exists ")
                    return render(request, 'Security_sign.html', {'key': 'username already exists'})
            else:
                User.objects.create_user(
                    username=Security_Id, email=Security_Email, password=Pas, first_name=Security_Name).save()
                user = User.objects.get(username=Security_Id)
            if user:
                if Security.objects.filter(SECURITY_NAME=Security_Id).exists():
                    print("user alerady exists ")
                    return render(request, 'Security_sign.html', {'key': 'user already exists'})
                else:
                    Security(SECURITYY=user, SECURITY_NAME=Security_Name,
                            SECURITY_PHONE=Security_Phone).save()
                    print('REGISTERED SUCCESSFULLY')
                    return redirect(security_log)
        else:
            print('password does not match')
            return render(request, 'Hod_sign.html', {'key': 'password does not match'})
    return render(request,'Security_sign.html')

#----------------Sign up ending-------------

#------------security login starting---------

def security_log(request):
    if request.method=='POST':
        Security_id=request.POST['security_id']
        Security_pass=request.POST['pass']
        if Security.objects.filter(SECURITYY__username=Security_id).exists():
            use=auth.authenticate(username=Security_id, password=Security_pass)
            if use is not None:
             auth.login(request,use)
             print('sucess login')
             return redirect(security_home)
            else:
             print('invalid')
             return render(request,'security_log.html',{'key':'INVALID USERNAME AND PASSWORD'})
        else:
             print('Not found')
             return render(request,'security_log.html',{'key':'USERNAME NOT FOUND'})
    return render(request,'security_log.html')

#------------security login ending---------

#------------------LOG OUT-----------------
#--------------------HOD------------------

def Hod_log_out(request):
    logout(request)
    return redirect(Hod_log)

#------------------Advisor---------------

def advisor_log_out(request):
    logout(request)
    return redirect(Advisor_log)

#------------------Security---------------

def security_log_out(request):
    logout(request)
    return redirect(security_log)

# -------------Profile view--------------
#-------------Advisor view---------------
def Advisor_profile(request):
    Advisor_pro=TEACHER.objects.get(Advisor=request.user)
    print( Advisor_pro.Advisor.username)
          
    return render(request,'Advisor_profile.html',{'key':Advisor_pro})


#--- adding students details-------------
def Student(request):
    return render(request,"Add_student.html")


