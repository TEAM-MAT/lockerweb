import code
from telnetlib import STATUS
from django.http.response import HttpResponse
from django.http.response import HttpResponseNotFound
import json
from locker.models import lockers
def reservation(user,locker):
    if locker.reserved==0:
        if user.lockernum is not None:#이미 예약한 사물함 존재
            oldlocker=user.lockernum
            oldlocker.reserved=0
            oldlocker.save()
            user.lockernum=None
        user.lockernum=locker
        user.lockernum.reserved=1
        user.save()
        locker.save()
        return HttpResponse("success")
    else:
        return HttpResponseNotFound("can't reserve")

def locker_info(user):
    userlocker=None
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
    context={"usercurrlocker":userlocker}
    return context

def locker_cancel(user):
    current_locker=user.lockernum
    if current_locker is not None:
        cl=current_locker.lockernum
        c=lockers.objects.get(lockernum=cl)
        c.reserved=0
        c.save()
        user.lockernum=None
        user.save()
        return HttpResponse(json.dumps({'code':200}))
    else:
        return HttpResponse(json.dumps({'code':404}))