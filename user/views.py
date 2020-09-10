from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import user as User
from django.urls import resolve
from django.http import HttpResponse
from datetime import datetime

# Global variables
Login=[]

# Create your views here.

# Dashboard
def dashboard(req):
    U=User.objects.get(usrEmailID=Login[0])
    return render(req,"user/dashboard/index.html",{"name":U.usrName,"desc":U.usrDescription})

# About me in Dashboard View
def me(req):
    return render(req,"user/dashboard/me/index.html",{})

#################################################################
# Login View
def login(req):
    if(req.method=="POST"):
        uname,psw=req.POST.get('username'),req.POST.get('pass')
        try:
            U=User.objects.get(usrEmailID=uname)
        except Exception:
            U=None
        if(U != None and U.password==psw):
            Login.append(U.usrEmailID)
            return redirect("/user")
        else: return HttpResponse("<h5>User Doesn't Exists... Please Register</h4> <br></br> <a href='/user/register'>Click Here to Register</a>")
    return render(req,"user/login/index.html",{})

# Forgot Password View
def forgot(req):
    if(req.method=="POST"):
        to_email = req.POST.get('email')
        U=User.objects.get(usrEmailID=to_email)
        U.usrStatus=99
        U.save()
        current_site = get_current_site(req)
        mail_subject = 'Reset Password - SCM'
        message = "Hello, %s \n\n We've recieved a Password Reset Request for your SCM Account. Kindly reset your Password by clicking the below link.\n\n Link: http://%s/user/reset/%s/ \n\n\n Regards:\nThe SCM Team\nContact Us: scm.tinktank@tinktank.com"%(to_email,str(current_site),oct(U.usrID)[2:])
        email = EmailMessage(mail_subject, message, to=[to_email,])
        email.send()
        return redirect("/user/reset_link_sent/")
    return render(req,"user/forgot/index.html",{})

# Reset Password Link Sent View
def reset_link_sent(req):
    return render(req,"user/reset_link_sent/index.html",{})

# Reset Password View
def reset(req):
    url_parts=req.path_info.split("/")
    uidb64=url_parts[-2]
    try:
        uID = int(uidb64,8)
        U = User.objects.get(usrID=uID)
    except Exception:U=None
    if(U is not None ):
        if(req.method=="POST"):
            psw1,psw2=req.POST.get("psw1"),req.POST.get("psw2")
            if(psw1==psw2):
                U.password=psw1
                U.usrStatus=1
                U.save()
            else:
                U.usrStatus=0
                U.save()
            mail_subject = 'Password Changed - SCM'
            message = "Hello, %s\n\n You have changed the password for your SCM Account \n\n\n Regards:\nThe SCM Team\nContact Us: scm.tinktank@gmail.com"%(U.usrEmailID)
            EmailMessage(mail_subject, message, to=[U.usrEmailID,]).send()
            return redirect("/user/reset-done")
    return render(req,"user/reset/index.html",{"email":U.usrEmailID})

# Reset Completed View
def reset_done(req):
    if(req.method=="POST"):
        return redirect("/user/login/")
    return render(req,"user/reset_done/index.html",{})

###########################################################################
# Registration Form
def register(req):
    if(req.method=="POST"):
        fname,lname,eID,ph,gender,city=req.POST.get("fname"),req.POST.get("lname"),req.POST.get("email"),req.POST.get("phone"),req.POST.get("gender"),req.POST.get("city")
        try:
            U=User.objects.get(usrEmailID=eID)
        except Exception:
            U=None
        if(U == None):
            No_of_objs=User.objects.all().count()
            U=User()
            U.usrEmailID=eID
            U.usrCity=city
            U.usrID=No_of_objs+1
            U.usrName=fname+" "+lname
            U.usrGender=gender
            U.usrPhone=ph
            U.usrCreationDate=datetime.now()
            U.password=""
            U.usrStatus=0
            U.usrDescription=""
            U.GoogleID=eID
            U.usrOrgName=""
            U.usrType="Normal"
            U.save()
            current_site = get_current_site(req)
            mail_subject = 'Registration Successful - SCM'
            message = "Hello, %s \n\n Welcome to Smart Contact Manager - SCM.\n\nYour SCM Account has been Successfully created\n\nFollow the below link to set your Password for your SCM Account and then follow the further Instructions.\n\n\n Link: http://%s/user/set_password/%s/ \n\n\n Regards:\nThe SCM Team\nContact Us: scm.tinktank@gmail.com"%(U.usrEmailID,str(current_site),oct(U.usrID)[2:])
            EmailMessage(mail_subject, message, to=[eID,]).send()
            return redirect("/user/verify_account/")
        else:return HttpResponse("<h5>User Already Exists... Please Login</h4> <br></br> <a href='/user/login'>Click Here to Login</a>")
    return render(req,"user/register/index.html",{})

# Verifying Account
def verify(req):
    return render(req,"user/verify/index.html",{})

# Setting New Password Completed View
def set_password_done(req):
    if(req.method=="POST"):
        return redirect("/user/login/")
    return render(req,"user/set_password_done/index.html",{})


# For Setting New Password View
def set_password(req):
    url_parts=req.path_info.split("/")
    uidb64=url_parts[-2]
    try:
        uID = int(uidb64,8)
        U = User.objects.get(usrID=uID)
    except Exception:U=None
    if(U is not None ):
        if(req.method=="POST"):
            psw1,psw2=req.POST.get("psw1"),req.POST.get("psw2")
            if(psw1==psw2):
                U.password=psw1
                U.usrStatus=1
                U.save()
            else:
                U.usrStatus=0
                U.save()
            mail_subject = 'Smart Contact Manager - SCM'
            message = "Hello, %s\n\n You have created a new password for your SCM Account\n\n Your SCM Account is now protected by your Encrypted Password.\n\n\n\n\n Regards:\nThe SCM Team\nContact Us: scm.tinktank@gmail.com"%(U.usrEmailID)
            EmailMessage(mail_subject, message, to=[U.usrEmailID,]).send()
            return redirect("/user/set_password_done/")
    return render(req,"user/set_password/index.html",{"email":U.usrEmailID})
