from django.urls import path
from . import views
from . import customviewfile

urlpatterns = [
    path('hello/', views.say_hello),
    path('sampling/', customviewfile.mycustomfunction)
]