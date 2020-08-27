from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(res):
    return HttpResponse(
        "<html><h1>This is Contact Importing</h1></html>"
    )