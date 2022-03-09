from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users
import json
from django.db import connection

@login_required(login_url='locker:login')
def reservePop(request):
    user=users.objects.get(id=request.user.id)
    userlocker=None
    if user.lockernum is not None:
        # userlocker=user.lockernum.lockernum
        _building = "";
        if user.lockernum.building == "HN":
            _building = "형남공학관 "
        elif user.lockernum.building == "IS":
            _building = "정보과학관 "
        elif user.lockernum.building == "CB":
            _building = "문화관 "

        userlocker= _building + str(user.lockernum.floor) +"층 " + str(user.lockernum.sector) +"구역 " + str(user.lockernum.written_lockernum) +"번 "
    context={"usercurrlocker":userlocker}
    return render(request,'locker/regist_popup.html', context)

@login_required
def reserve(request):#예약
    if request.method=="POST":
        user=request.user
        locknum=json.loads(request.body.decode("utf-8"))
        locker=lockers.objects.get(lockernum=locknum['lockernum'])
        if locker.reserved==0:
            if user.lockernum is not None:#이미 예약한 사물함 존재
                oldlocker=user.lockernum
                oldlocker.reserved=0
                oldlocker.save()
                user.lockernum=None
            user.lockernum=locker
            user.lockernum.reserved=1
            user.save()
            locker.save()
            return HttpResponse(json.dumps({'code':200}))
        else:
            return HttpResponse(json.dumps({'code':404}))

@login_required(login_url='locker:login')
def cancelPop(request):
    user=users.objects.get(id=request.user.id)
    userlocker=None
    if user.lockernum is not None:
        # userlocker=user.lockernum.lockernum
        _building = "";
        if user.lockernum.building == "HN":
            _building = "형남공학관 "
        elif user.lockernum.building == "IS":
            _building = "정보과학관 "
        elif user.lockernum.building == "CB":
            _building = "문화관 "

        userlocker= _building + str(user.lockernum.floor) +"층 " + str(user.lockernum.sector) +"구역 " + str(user.lockernum.written_lockernum) +"번 "
    context={"usercurrlocker":userlocker}
    return render(request,'locker/cancel_popup.html', context)

@login_required(login_url='locker:login')
def cancel(request):
    if request.method=="POST":
        user=users.objects.get(id=request.user.id)
        current_locker=user.lockernum
        if current_locker is not None:
            cl=current_locker.lockernum
            c=lockers.objects.get(lockernum=cl)
            c.reserved=0
            c.save()
            user.lockernum=None
            user.save()
            return HttpResponse(json.dumps({'code':200}))
        else:
            return HttpResponse(json.dumps({'code':404}))