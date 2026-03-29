from django.shortcuts import render, redirect
# connecting models
from . models import *
# connecting Athenticaton Table
from django.contrib.auth.models import User, auth
# log out
from django.contrib.auth import logout
# Current Date
from datetime import date, datetime

from django.http import JsonResponse



# phone calls/
# import requests
from twilio.rest import Client
from django.conf import settings


# -------scanning barcode----------


# from .models import Student

# Create your views here.

# -----------HOMES------------------

def home(request):
    return render(request, 'Aa_main.html')


def advisor_home(request):
    Advisor_pro = TEACHER.objects.get(Advisor=request.user)
    print(Advisor_pro.Advisor.username)
    return render(request, 'Advisor_home.html', {'key': Advisor_pro})


def hod_home(request):
    HOD_pro = HOD.objects.get(HOD=request.user)
    print(HOD_pro.HOD.username)
    today = date.today()
    print(today)    
    gppp=Gate_Pass.objects.filter(HOD_APPROVE='NO',gate_date=today)
    gcount=gppp.count()
    print(gcount)  
    
    context={'key': HOD_pro,'key1':gcount}
    return render(request, 'Hod_home.html', context)


def security_home(request):
    SER_pro = Security.objects.get(SECURITYY=request.user)
    print(SER_pro.SECURITY_NAME)
    return render(request, 'Security_home.html', {'key': SER_pro})

# -----ADVISOR LOGIN AND SIGN UP-------

# ---------Sign up starting------------


def Advisor_sign(request):
    if request.method == 'POST':
        Teacher_Name = request.POST['teacher_name']
        Teacher_Id = request.POST['teacher_id']
        Teacher_Email = request.POST['teacher_email']
        Teacher_Phone = request.POST['teacher_phone']
        Teacher_dept = request.POST['teacher_dept'].upper()
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
                            TEACHER_PHONE=Teacher_Phone, TEACHER_DEPT=Teacher_dept).save()
                    print('REGISTERED SUCCESSFULLY')
                    return redirect(Advisor_log)
        else:
            print('password does not match')
            return render(request, 'Advisor_sign_in.html', {'key': 'password does not match'})
    return render(request, 'Advisor_sign_in.html')
  # return render(request,'Advisor_sign _in.html')

# ---------Sign up ending------------

# ---------login Starting------------


def Advisor_log(request):
    if request.method == 'POST':
        adv_id = request.POST['Ad_id']
        advi_pass = request.POST['pass']
        if TEACHER.objects.filter(Advisor__username=adv_id).exists():
            use = auth.authenticate(username=adv_id, password=advi_pass)
            if use is not None:
                auth.login(request, use)
                print('sucess login')
                return redirect(advisor_home)
            else:
                print('invalid')
                return render(request, 'Advisor_log_in.html', {'key': 'INVALID USERNAME AND PASSWORD'})
        else:
            print('Not found')
            return render(request, 'Advisor_log_in.html', {'key': 'USERNAME NOT FOUND'})
    return render(request, 'Advisor_log_in.html')

# -----------login ending--------------

# -----------HOD LOGIN/SIGN UP---------

# -----------sign up start-------------


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
    return render(request, 'Hod_sign.html')

# ----------------Sign up ending-------------

# -------------HOD login starting-------------


def Hod_log(request):
    if request.method == 'POST':
        hod_id = request.POST['hod_id']
        hod_pass = request.POST['pass']
        if HOD.objects.filter(HOD__username=hod_id).exists():
            use = auth.authenticate(username=hod_id, password=hod_pass)
            if use is not None:
                auth.login(request, use)
                print('sucess login')
                return redirect(hod_home)
            else:
                print('invalid')
                return render(request, 'HOd_log.html', {'key': 'INVALID USERNAME AND PASSWORD'})
        else:
            print('Not found')
            return render(request, 'HOd_log.html', {'key': 'USERNAME NOT FOUND'})
    return render(request, 'Hod_log.html')

# ----------------login ending-------------

# -----------SECURITY LOGIN/SIGN UP--------

# --------------sign up start--------------


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
    return render(request, 'Security_sign.html')

# ----------------Sign up ending-------------

# ------------security login starting---------


def security_log(request):
    if request.method == 'POST':
        Security_id = request.POST['security_id']
        Security_pass = request.POST['pass']
        if Security.objects.filter(SECURITYY__username=Security_id).exists():
            use = auth.authenticate(
                username=Security_id, password=Security_pass)
            if use is not None:
                auth.login(request, use)
                print('sucess login')
                return redirect(security_home)
            else:
                print('invalid')
                return render(request, 'security_log.html', {'key': 'INVALID USERNAME AND PASSWORD'})
        else:
            print('Not found')
            return render(request, 'security_log.html', {'key': 'USERNAME NOT FOUND'})
    return render(request, 'security_log.html')

# ------------security login ending---------

# ------------------LOG OUT-----------------
# --------------------HOD------------------


def Hod_log_out(request):
    logout(request)
    return redirect(Hod_log)

# ------------------Advisor---------------


def advisor_log_out(request):
    logout(request)
    return redirect(Advisor_log)

# ------------------Security---------------


def security_log_out(request):
    logout(request)
    return redirect(security_log)
# ---------------------------------------------------------------------Advisor room----------------------------------------------------------------------
# -------------Profile view--------------
# -------------Advisor view---------------


def Advisor_profile(request):
    Advisor_pro = TEACHER.objects.get(Advisor=request.user)
    print(Advisor_pro.Advisor.username)

    return render(request, 'Advisor_profile.html', {'key': Advisor_pro})


# --- Adding students details-------------
def Add_students_details(request):
    user = TEACHER.objects.get(Advisor__username=request.user)
    if request.method == 'POST':
        Std_name = request.POST['St_name']
        Add_no = request.POST['Ad_no']
        Depart = request.POST['Dept']
        Branch_name = request.POST['Branch'].upper()
        Year = request.POST['Year']
        Phone_no1 = request.POST['Phone1']
        Phone_no2 = request.POST['Phone2']
        print(Add_no)
        Details_students(TEACHER_NAME=user, ADMISSION_NO=Add_no, NAME=Std_name, DEPARTMENT=Depart,
                         BRANCH=Branch_name, YEAR=Year, PHONE1=Phone_no1, PHONE2=Phone_no2).save()

        return redirect(advisor_home)
    return render(request, 'Add_students_details.html')

# ------Student requsting----------------

def Student_requsting(request, admission_no):
    TEACHERS = TEACHER.objects.get(Advisor=request.user)
    print(TEACHERS.Advisor.id)

    STUDENT = Details_students.objects.get(ADMISSION_NO=admission_no,
        TEACHER_NAME__Advisor__id=TEACHERS.Advisor.id)
    print(STUDENT)

    context = {'key': STUDENT, 'keys': TEACHERS}

    if request.method == 'POST':
        st_name = request.POST['Name']
        st_branch = request.POST['Branch']
        st_year = request.POST['Year']
        st_phone = request.POST['Phone_no1']   
        Reasons = request.POST['Reason']       
        Approved = request.POST['approved']
        st_admission = request.POST['Admission']
        teacher_name = request.POST['Teacher_name']

        # Save Gate Pass
        Gate_Pass(
            STUD_NAME=st_name,
            STUD_BRANCH=st_branch,
            STUD_YEAR=st_year,
            STUD_PHONE1=st_phone,
            APPORVED=Approved,
            TEACHER_ID=TEACHERS,
            STUDENT_ID=STUDENT,
            REASONS=Reasons
        ).save()




        return render(request, "Advisor_student_barcode_search.html",
                      {'key': 'GATE PASS REQUESTED TO HOD'})

    
    return render(request, 'Details_student.html', context)


# -----Searching with Barcode of teacher-------

def Advisor_student_barcode_search(request):
    TEACHERS = TEACHER.objects.get(Advisor=request.user)
    if request.method == 'POST':
        Scanned = request.POST['barcode']
        teacher = request.POST['ad']
        print(Scanned)
        if Details_students.objects.filter(TEACHER_NAME=TEACHERS):
            print(teacher)
            print(TEACHERS.TEACHER_DEPT)
            student = Details_students.objects.get(ADMISSION_NO=Scanned,BRANCH=TEACHERS.TEACHER_DEPT)

                
            if int(student.ADMISSION_NO) == int(Scanned):
                today = date.today()
                print(today)

                SeGate = Gate_Pass.objects.filter(STUDENT_ID__ADMISSION_NO=Scanned,gate_date=today)

                # ✅ check if record exists
                if SeGate.exists():
                     return render(request,"Advisor_student_barcode_search.html",{'key': 'ALREADY GATE PASS ISSUED TODAY'})
                else:
                    print("Entered")
                    return redirect(Student_requsting, admission_no=Scanned)
            else:
                print("add student")
                return redirect(Add_students_details)
        else:
            print("add student")
            return redirect(Add_students_details)
    else:
        return render(request, "Advisor_student_barcode_search.html", {'keys': TEACHERS})
    return render(request, "Advisor_student_barcode_search.html")
# return render(request,"Advisor_student_barcode_search.html",{'keys':TEACHERS})


def Advisor_admission(request):
    TEACHERS = TEACHER.objects.get(Advisor=request.user)
    if request.method == 'POST':
        Scanned = request.POST['barcode']
        teacher = request.POST['ad']
        print(Scanned)
        if Details_students.objects.filter(TEACHER_NAME=TEACHERS):
            print(teacher)
            print(TEACHERS.TEACHER_DEPT)
            student = Details_students.objects.get(ADMISSION_NO=Scanned,BRANCH=TEACHERS.TEACHER_DEPT)

                
            if int(student.ADMISSION_NO) == int(Scanned):
                today = date.today()
                print(today)

                SeGate = Gate_Pass.objects.filter(STUDENT_ID__ADMISSION_NO=Scanned,gate_date=today)

                # ✅ check if record exists
                if SeGate.exists():
                     return render(request,"Advisor_admission.html",{'key': 'ALREADY GATE PASS ISSUED TODAY'})
                else:
                    print("Entered")
                    return redirect(Student_requsting, admission_no=Scanned)
            else:
                print("add student")
                return redirect(Add_students_details)
        else:
            print("add student")
            return redirect(Add_students_details)
    else:
        return render(request, "Advisor_admission.html", {'keys': TEACHERS})
    return render(request, "Advisor_admission.html")
# return render(request,"Advisor_student_barcode_search.html",{'keys':TEACHERS})
    

# THIS LAST TWO FUNCTIONS ARE MADE FOR EXPO THIS NOT SET IN REAL PROJECT
def redooo(request):
    today = date.today()
    print(today)
    SeGate = Gate_Pass.objects.filter(
        # latest record first
        gate_date=today, ).order_by('-id')
    return render(request,"redooo.html", {'key': SeGate})

def rdRejectss(request, pk):
    gatte = Gate_Pass.objects.filter(id=pk)
    gatte.delete()
    return redirect(redooo)
# ----------------------------------------------------------------
# ------------------------------------------------------------------Security room----------------------------------------------------------------------
def Security_Barcode(request):
    SECURITY = Security.objects.get(SECURITYY=request.user)

    if request.method == 'POST':
        Scanned = request.POST.get('barcode')
        print(Scanned)

        try:
            # ✅ get correct student
            student = Details_students.objects.get(ADMISSION_NO=Scanned)
        except Details_students.DoesNotExist:
            return render(request, 'Security_Barcode.html', {'key': "Not registered"})

        today = date.today()

        try:
            SeGate = Gate_Pass.objects.filter(
                STUDENT_ID__ADMISSION_NO=Scanned
            ).latest('gate_date')
        except Gate_Pass.DoesNotExist:
            return render(request, "Security_Barcode.html", {'key': "NO GATE PASS"})

        print("HAI")
        print(SeGate.exit_time)

        if SeGate.gate_date == today:

            if SeGate.HOD_APPROVE == "yes" and SeGate.exit_time is None:
                print("Entered")

                context = {
                    'keys': SeGate,
                    'key1': SECURITY,
                }
                return render(request, "Security_Approval.html", context)

            else:
                return render(request, "Security_Barcode.html", {'key': "HOD IS NOT APPROVED"})
        else:
            return render(request, "Security_Barcode.html", {'key': "NO GATE PASS"})

    return render(request, "Security_Barcode.html", {'keys': SECURITY})


def Security_re_entry_scan(request):
    SECURITY = Security.objects.get(SECURITYY=request.user)

    if request.method == 'POST':
        Scanned = request.POST.get('barcode')
        print(Scanned)

        try:
            # ✅ Get correct student
            student = Details_students.objects.get(ADMISSION_NO=Scanned)
        except Details_students.DoesNotExist:
            return render(request, 'Security_re_entry_scan.html', {'key': "Not registered"})

        today = date.today()

        try:
            SeGate = Gate_Pass.objects.filter(
                STUDENT_ID__ADMISSION_NO=Scanned
            ).latest('gate_date')
        except Gate_Pass.DoesNotExist:
            return render(request, "Security_re_entry_scan.html", {'key': "No Gate Pass"})

        print("?????", SeGate.gate_date)
        print(SeGate.re_enrty_time)

        if SeGate.gate_date == today:

            if SeGate.HOD_APPROVE == "yes" and SeGate.re_enrty_time is None:
                print("Entered")

                context = {
                    'keys': SeGate,
                    'key1': SECURITY
                }
                return render(request, "Security_re_entry.html", context)

            else:
                return render(request, "Security_re_entry_scan.html", {'key': "Already entry"})

        else:
            return render(request, "Security_re_entry_scan.html", {'key': "Already entry"})

    return render(request, "Security_re_entry_scan.html", {'keys': SECURITY})


def checks(request, pk):
    gatte = Gate_Pass.objects.get(id=pk)
    Gate_time = datetime.now().time()
    gatte.exit_time = Gate_time
    print(Gate_time)
    gatte.save()
    return redirect(Security_Barcode)


def re_entry(request, pk):
    gatte = Gate_Pass.objects.get(id=pk)
    Gate_time = datetime.now().time()
    gatte.re_enrty_time = Gate_time
    print(Gate_time)
    gatte.save()
    return redirect(Security_re_entry_scan)
    return redirect()


def Security_Approval(request):
    return render(request, "Security_Approval.html")


def Security_re_entry(request):
    return render(request, "Security_re_entry.html")

# --------barcode reader---------------------


def save_student(request):
    # barcode = request.POST.get('barcode')
    # return JsonResponse({'barcode': barcode})
    return render(request, 'Add_student.html')

# ---------------------------------------------------------------HOD Room----------------------------------------------------------------------------
def Hod_tr_Approval(request):
    return render(request,"Hod_tr_Approval.html")
def gatelist(request):
    gppp=Gate_Pass.objects.filter(HOD_APPROVE='yes',exit_time__isnull=False)
    gcount=gppp.count()
    print(gcount)    
    return render(request,"Hod_gatelist.html",{'key':gppp})


def Hod_st_approval(request):
    today = date.today()
    print(today)
    SeGate = Gate_Pass.objects.filter(
        # latest record first
        gate_date=today, HOD_APPROVE="NO").order_by('-id')

        

        
    return render(request, "Hod_st_approval.html", {'key': SeGate})


def pay_accepts(request, pk):
    gatte = Gate_Pass.objects.get(id=pk)
    gatte.HOD_APPROVE = "yes"
    gatte.save()

    from twilio.rest import Client

    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    message = f"Issuing Gate Pass to {gatte.STUD_NAME} to leave the college. Reason: {gatte.REASONS}"

    # ✅ get phone from DB (NOT request)
    phone = gatte.STUD_PHONE1

    phone = phone.strip()
    phone = ''.join(filter(str.isdigit, phone))

    to = "+91" + phone

    print("Sending to:", to)

    sms = client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to
    )

    return redirect(Hod_st_approval)

def pay_Rejects(request, pk):

    gatte = Gate_Pass.objects.filter(id=pk)
    gatte.delete()
    return redirect(Hod_st_approval)
# ----- live clock----------------------------


# def live_clock(request):
#     return render(request, "live_clock.html")


# phone calls
def send_sms(phone, message):
    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone
    )
# FAST2SMS_API_KEY = "doG1RxJc3eVITWFjX4ialPDgE8UNB7LtmkCK52SO9ufYzQbsnqdPXnj9b2HA8yUM0IlTw7iY4LKSvC35"


# def send_sms(phone, message):
#     url = "https://www.fast2sms.com/dev/bulkV2"

#     payload = {
#         "route": "q",
#         "message": message,
#         "numbers": phone
#     }

#     headers = {
#         "authorization": FAST2SMS_API_KEY,
#         "Content-Type": "application/json"
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()
