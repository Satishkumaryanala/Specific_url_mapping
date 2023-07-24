#  Modules important for creating url mapping
from django.urls import path
from app2.views import *

app_name='second somthing'

urlpatterns =[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]