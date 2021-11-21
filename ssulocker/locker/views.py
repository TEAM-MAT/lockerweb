from django.shortcuts import render
#from django.http import HttpResponse
from .models import lockers
def index(request):
    return render(request,'locker/index.html')
def lockerlist(request):
    locker_list=lockers.objects.order_by('lockernum')
    context={"locker_list":locker_list}
    return render(request,'locker/lockerlist.html',context)
# Create your views here.
