from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users
from ..middleware.time_login import timecheck
from locker.api.locker_api import locker_info
from django.db import connection
@login_required(login_url='locker:login')
def lockerlist(request):
    if request.user.is_authenticated:
        if timecheck(request.user.department)==1:
            user=users.objects.get(id=request.user.id)
            locker_list=lockers.objects.filter(department=user.department,reserved=0).order_by("lockernum")   
            reservation_before=locker_info(user)
            if reservation_before["usercurrlocker"] is None:
                userlocker="예약된 사물함 없음"
            else:
                userlocker=reservation_before["usercurrlocker"]
            context={"locker_list":locker_list,"department":user.department,"username":user.name,"usercurrlocker":userlocker}
            return render(request,'locker/lockerlist.html',context)
        else:
            auth.logout(request)
            return redirect('/locker/login')
    else:
        return redirect('/locker/login')
