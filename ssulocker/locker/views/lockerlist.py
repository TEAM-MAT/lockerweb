from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users
from .time_login import timecheck
import logging
import json
from django.db import connection
@login_required(login_url='locker:login')
def lockerlist(request):
    if request.user.is_authenticated:
        if timecheck(request.user.department)==1:
            user=users.objects.get(id=request.user.id)
            locker_list=lockers.objects.filter(department=user.department,reserved=0).order_by("lockernum")   
            userlocker="예약된 사물함 없음"
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
            context={"locker_list":locker_list,"department":user.department,"username":user.name,"usercurrlocker":userlocker}
            return render(request,'locker/lockerlist.html',context)
        else:
            auth.logout(request)
            return redirect('/locker/login')
    else:
        return redirect('/locker/login')
