from django.shortcuts import render
from django.http import HttpResponse
from .models import locker
def index(request):
    locker_list=locker.objects.order_by('lockernum')
    context={"사물함리스트:":locker_list}
    return render(request,'locker/lockerlist.html',context)
# Create your views here.
