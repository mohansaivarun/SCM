from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard(res):
    reg="<a href=user/register>Register</a>"
    log="<a href=user/login>Login</a>"
    return HttpResponse(
        "<html><h1>This is User Dashboard</h1>"+str(reg)+"<br></br>"+str(log)+"</html>"
    ) 

def register(res):
    return render(res,"user/register/index.html",{})

def login(res):
    return render(res,"user/login/index.html",{})