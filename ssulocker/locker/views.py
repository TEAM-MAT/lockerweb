from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404
import django.contrib.auth as aut
#from django.http import HttpResponse
from .models import lockers
from django.db import connection
def index(request):
    #학부 별 남은라커 수/라커 수 구해서 띄워줄 것임.
    CS_left=lockers.objects.filter(department="CS",reserved=0).count()
    CS_lockers=lockers.objects.filter(department="CS").count()
    context={"CS_left":CS_left,"CS_lockers":CS_lockers}
    return render(request,'locker/index.html',context)
def lockerlist(request):
    locker_list=lockers.objects.order_by('lockernum')
    context={"locker_list":locker_list}
    return render(request,'locker/lockerlist.html',context)
        
# Create your views here.
