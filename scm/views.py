from django.shortcuts import render

def sample(res):
    return render(res,"user/pre/index.html",{})