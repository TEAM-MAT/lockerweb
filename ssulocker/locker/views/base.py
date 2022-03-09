from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users,department
from django.db import connection
from ..middleware.time_login import timecheck
from ..api import base_context
def index(request):
    locker_context=base_context.base_context_return()
    if request.method=="POST" and not request.user.is_authenticated:
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
    elif request.method=="POST" and request.user.is_authenticated:
        locker_context['multiuser']=1
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