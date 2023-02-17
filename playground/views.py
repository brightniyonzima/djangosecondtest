from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])

    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

    for x in thislist:
        print(x)

    return HttpResponse('Hello Django!')

# Create your views here.
