from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404
import django.contrib.auth as aut
#from django.http import HttpResponse
from .models import lockers
def index(request):
    return render(request,'locker/index.html')
def lockerlist(request):
    locker_list=lockers.objects.order_by('lockernum')
    context={"locker_list":locker_list}
    return render(request,'locker/lockerlist.html',context)
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=aut.authenticate(request,username=username,passord=password)
        
# Create your views here.
