from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404
import django.contrib.auth as aut
#from django.http import HttpResponse
from .models import lockers
import logging
from django.db import connection
def index(request):
    #학부 별 남은라커 수/라커 수 구해서 띄워줄 것임.
    CS_left=lockers.objects.filter(department="CS",resreved=0).count()
    CS_lockers=lockers.objects.filter(department="CS").count()
    locker_context={"cs_left":CS_left,"cs_lockers":CS_lockers}
    return render(request,'locker/index.html',locker_context)
def lockerlist(request):
    locker_list=lockers.objects.order_by('lockernum')
    context={"locker_list":locker_list}
    return render(request,'locker/lockerlist.html',context)
def registpop(request):
    return render(request,'locker/regist_popup.html')
# Create your views here.
