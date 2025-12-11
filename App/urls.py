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
    path('Hod log out',views.Hod_log_out),

    #-----------Advisor------------
    path('Advisor log out',views.advisor_log_out), 

    #-----------Security-----------
    path('Security log out',views.security_log_out),    

]