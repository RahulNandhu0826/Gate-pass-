from django.urls import path
from . import views
urlpatterns= [
    #--------------HOME PAGES-------------

    path('',views.home),
    path('Advisor_home',views.advisor_home),
    path('Hod_Home',views.hod_home),
    path('Security_Home',views.security_home),
    

    #----------login /sign pages----------
    
    #-----------Advisors-----------------

    path('Advisor_sign',views.Advisor_sign),
    path('Advisor_log',views.Advisor_log),

    #-----------HOD--------------
    path('Hod_sign',views.Hod_sign),
    path('Hod_log',views.Hod_log),  

    #-----------Security----------
    path('Security_sign',views.security_sign),
    path('Security_log',views.security_log),  

    #-----------LOG OUTS-----------Hod_log

    #-----------Advisor------------
    path('Hodlogout',views.Hod_log_out),

    #-----------Advisor------------
    path('Advisorlogout',views.advisor_log_out), 

    #-----------Security-----------
    path('Securitylogout',views.security_log_out),  
    #-----------------------------------------------Advisor Room------------------------------------------------------------------------------------
    #-------student request-------
    path('Student_requsting<str:admission_no>', views.Student_requsting ,name='student_req'),

    #--Advisor_student_barcode_search--

    path('Advisor_student_barcode_search',views.Advisor_student_barcode_search), 
    
    #------------Pofile Views--------

    path('Advisor_profile',views.Advisor_profile),

    #-----------Add Students----------

    path('Add_students_details',views.Add_students_details),

    #----------Advisor request Student barcode-------

    path('save/', views.save_student, name='save_student'),


    #--------------without id card---------------------------
    path('Advisor_admission',views.Advisor_admission),

    path('redooo',views.redooo),
    
    path('rdRejectss<str:pk>',views.rdRejectss,name='rdRejectss'),

    #-----------------------------------------------------------------------Security Room-----------------------------------------------------------
    #---------Security requst  barcode---------------
    
    path('Security_Barcode',views.Security_Barcode),
    
    path('Security_Approval',views.Security_Approval),
    path('Security_re_entry_scan',views.Security_re_entry_scan),
    
    path('Security_re_entry',views.Security_re_entry),
    #--------------------premission approval--------------------------
    path('check<str:pk>',views.checks,name='checks'),
    path('re_entry<str:pk>',views.re_entry,name='re_entrys'),
    #----------------------------------------------------------------------HOD Room-----------------------------------------------------------------

    
    path('Hod_st_approval',views.Hod_st_approval),
    path('Hod_tr_Approval',views.Hod_tr_Approval),
    path('Gate_list',views.gatelist),
   
    #--------------------premission approval--------------------------
    path('pay_accepts<str:pk>',views.pay_accepts,name='pay_acceptss'),
    path('pay_Rejects<str:pk>',views.pay_Rejects,name='pay_Rejectss'),

    path('students', views.student_list),
   
   

    #----------Live Clock------------
    # path("clock/", views.live_clock, name="live_clock"),

]