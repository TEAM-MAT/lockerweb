from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
#from django.http import HttpResponse
from .models import lockers,users
import logging
from django.db import connection
def index(request):
    #학부 별 남은라커 수/라커 수 구해서 띄워줄 것임.
    cs_left=lockers.objects.filter(department="CS",reserved=0).count()
    cs_lockers=lockers.objects.filter(department="CS").count()
    ee_left=lockers.objects.filter(department="EIE",reserved=0).count()
    ee_lockers=lockers.objects.filter(department='EIE').count()
    gm_left=lockers.objects.filter(department='GM',reserved=0).count()
    gm_lockers=lockers.objects.filter(department='GM').count()
    sw_left=lockers.objects.filter(department='SW',reserved=0).count()
    sw_lockers=lockers.objects.filter(department="SW").count()
    AIC_left=lockers.objects.filter(department="AIC",reserved=0).count()
    AIC_lockers=lockers.objects.filter(department="AIC").count()
    locker_context={"cs_left":cs_left,"cs_lockers":cs_lockers,'eie_left':ee_left,'eie_lockers':ee_lockers,
    'gm_left':gm_left,'gm_lockers':gm_lockers,'sw_left':sw_left,'sw_lockers':sw_lockers,
    'AI_left':AIC_left,'AI_lockers':AIC_lockers}
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
    if request.user.is_authenticated:
        user=users.objects.get(id=request.user)
        locker_list=lockers.objects.filter(department=user.department).order_by("lockernum")
        context={"locker_list":locker_list,"department":user.department}
        return render(request,'locker/lockerlist.html',context)
    else:
        return redirect('/locker/login')
def registpop(request):
    return render(request,'locker/regist_popup.html')
# Create your views here.
