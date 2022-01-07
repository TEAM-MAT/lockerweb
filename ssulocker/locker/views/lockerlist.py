from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users
import logging
import json
from django.db import connection
@login_required(login_url='locker:login')
def lockerlist(request):
    if request.user.is_authenticated:
        user=users.objects.get(id=request.user.id)
        locker_list=lockers.objects.filter(department=user.department,reserved=0).order_by("lockernum")   
        userlocker="예약된 사물함 없음"
        if user.lockernum is not None:
            userlocker=user.lockernum.lockernum
        context={"locker_list":locker_list,"department":user.department,"username":user.name,"usercurrlocker":userlocker}
        return render(request,'locker/lockerlist.html',context)
    else:
        return redirect('/locker/login')
