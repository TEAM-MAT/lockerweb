from ..models import users,department
import datetime
def timecheck(usrdept):
    if datetime.datetime.now()>=department.getdepttime(usrdept):
        token=1
    else:
        token=0
    return token