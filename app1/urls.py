# Modules important for to create ulrs mapping
from django.urls import path
from app1.views import *
app_name='Somthing....'

from app1.views import *

# uls mapping

urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]