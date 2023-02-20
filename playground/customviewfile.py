from django.shortcuts import render
from django.http import HttpResponse

def mycustomfunction(self):
    return HttpResponse('right here in custom view file')