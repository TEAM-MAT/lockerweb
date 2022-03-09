from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users
import json
from locker.api import reservation,locker_info,locker_cancel


@login_required(login_url='locker:login')
def reservePop(request):
    user=users.objects.get(id=request.user.id)
    context=locker_info(user)
    return render(request,'locker/regist_popup.html', context)

@login_required
def reserve(request):#예약
    if request.method=="POST":
        user=request.user
        locknum=json.loads(request.body.decode("utf-8"))
        locker=lockers.objects.get(lockernum=locknum['lockernum'])
        result=reservation(user,locker)
        return result

@login_required(login_url='locker:login')
def cancelPop(request):
    user=users.objects.get(id=request.user.id)
    context=locker_info(user)
    return render(request,'locker/cancel_popup.html', context)

@login_required(login_url='locker:login')
def cancel(request):
    if request.method=="POST":
        user=users.objects.get(id=request.user.id)
        result = locker_cancel(user)
        return result