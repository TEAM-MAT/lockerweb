from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
#from django.http import HttpResponse
from .models import lockers
import logging
from django.db import connection
def index(request):
    #학부 별 남은라커 수/라커 수 구해서 띄워줄 것임.
    cs_left=lockers.objects.filter(department="CS",reserved=0).count()
    cs_lockers=lockers.objects.filter(department="CS").count()
    locker_context={"cs_left":cs_left,"cs_lockers":cs_lockers}
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/locker/lockerlist')
        else:
            return render(request,'locker/index.html',{'error':'아이디 또는 패스워드가 일치하지 않습니다'})
    else:
        return render(request,'locker/index.html',locker_context)
def lockerlist(request):
    locker_list=lockers.objects.order_by('lockernum')
    context={"locker_list":locker_list}
    return render(request,'locker/lockerlist.html',context)
def registpop(request):
    return render(request,'locker/regist_popup.html')
# Create your views here.
