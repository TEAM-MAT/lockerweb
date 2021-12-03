from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404
import django.contrib.auth as aut
#from django.http import HttpResponse
from .models import lockers
from django.db import connection
def index(request):
    #학부 별 남은라커 수/라커 수 구해서 띄워줄 것임.
    CS_reserved=lockers.objects.filter(department="CS" , reserved=1).count('lockernum')
    CS_lockers=lockers.objects.filter(department="CS").count('lockernum')
    return render(request,'locker/index.html')
def lockerlist(request):
    locker_list=lockers.objects.order_by('lockernum')
    context={"locker_list":locker_list}
    return render(request,'locker/lockerlist.html',context)
        
# Create your views here.
