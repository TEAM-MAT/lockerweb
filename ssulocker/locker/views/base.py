from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users,department
from django.db import connection
from .time_login import timecheck
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
    cs_time=department.objects.get(deptname="CS").time
    eie_time=department.objects.get(deptname="EIE").time
    gm_time=department.objects.get(deptname="GM").time
    sw_time=department.objects.get(deptname="SW").time
    aic_time=department.objects.get(deptname="AIC").time
    cs_fin=department.objects.get(deptname="CS").fintime
    eie_fin=department.objects.get(deptname="EIE").fintime
    sw_fin=department.objects.get(deptname="SW").fintime
    gm_fin=department.objects.get(deptname="GM").fintime
    aic_fin=department.objects.get(deptname="AIC").fintime
    cs_contact=department.objects.get(deptname="CS").contact
    eie_contact=department.objects.get(deptname="EIE").contact
    gm_contact=department.objects.get(deptname="GM").contact
    aic_contact=department.objects.get(deptname="AIC").contact
    sw_contact=department.objects.get(deptname="SW").contact
    days=["월","화","수","목","금","토","일"]
    class dept_weekdays():
        eie_day=days[eie_time.weekday()]
        cs_day=days[cs_time.weekday()]
        gm_day=days[gm_time.weekday()]
        sw_day=days[sw_time.weekday()]
        aic_day=days[aic_time.weekday()]
    locker_context={"cs_left":cs_left,"cs_lockers":cs_lockers,'eie_left':ee_left,'eie_lockers':ee_lockers,
    'gm_left':gm_left,'gm_lockers':gm_lockers,'sw_left':sw_left,'sw_lockers':sw_lockers,
    'AI_left':AIC_left,'AI_lockers':AIC_lockers,"cs_time":cs_time,"eie_time":eie_time,"gm_time":gm_time,
    "sw_time":sw_time,"aic_time":aic_time,"days":dept_weekdays,"time_token":1,"cs_contact":cs_contact,"eie_contact":eie_contact,"gm_contact":gm_contact,
    "aic_contact":aic_contact,"sw_contact":sw_contact,"eie_fin":eie_fin,"cs_fin":cs_fin,"gm_fin":gm_fin,"sw_fin":
    sw_fin,"aic_fin":aic_fin}
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            token=timecheck(user.department)
            if token==1:
                return redirect('/locker/lockerlist')
            else:
                locker_context["time_token"]=0
                auth.logout(request)
                return render(request,'locker/index.html',locker_context)
        else:
            locker_context['error']=1
            return render(request,'locker/index.html',locker_context)
    else:
        if request.user.is_authenticated:
            return redirect('/locker/lockerlist')
        else:
            return render(request,'locker/index.html',locker_context)

@login_required(login_url='locker:login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/locker/login')