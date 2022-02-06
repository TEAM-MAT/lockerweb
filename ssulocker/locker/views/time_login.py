from ..models import users,department
import datetime
def timecheck(usrdept):
    if datetime.datetime.now()>=department.getdepttime(usrdept):#예약시간 이후면
        if department.getdeptfintime(usrdept)>datetime.datetime.now(): #예약시간으로부터 22시간 까지 예약가능.
            token=1
        else:
            token=0
    else:
        token=0
    return token