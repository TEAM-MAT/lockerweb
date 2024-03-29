from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.db import models
from importlib import import_module
from threading import Thread
import datetime
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
departments=[('CS','컴퓨터학부'),
    ('GM','글로벌미디어학부'),('EIE','전자정보공학부'),('SW','소프트웨어학부'),
    ('AIC','AI융합학부')]
buildings=[('HN','형남공학관'),('IS','정보과학관'),('CB','문화관')]
class department(models.Model):
    deptname=models.CharField(max_length=6,choices=departments,primary_key=True)
    time=models.DateTimeField(help_text="예약시작날짜",default=datetime.datetime.now())#예약시작날짜 &시간
    fintime=models.DateTimeField(help_text="예약 종료 날짜",default=datetime.datetime.now()+datetime.timedelta(hours=120))#예약 종료 날짜 & 시간
    contact=models.CharField(max_length=100)
    def getdepttime(self):
        return self.time
    def getdeptfintime(self):
        return self.fintime

class departmentset():
    @staticmethod
    def departmentset():
        for i in range(5):
            temp=department(deptname=departments[i][0],time=datetime.datetime.now(),fintime=datetime.datetime.now()+datetime.timedelta(days=20))
            temp.save()

class lockers(models.Model):
    lockernum=models.CharField(max_length=10,primary_key=True)#건물앞글자+층+섹터+번호 조합해서 만들기
    written_lockernum=models.IntegerField(default='0')
    floor=models.IntegerField(default=1)
    reserved=models.IntegerField(default=0)#reserved -> 1 unreserved ->0,trigger로 바꿔줘야할듯
    sector=models.CharField(max_length=2,help_text='층별 구역',default='A')
    building=models.CharField(max_length=6,choices=buildings,default='IS')
    department=ForeignKey(department,related_name="lockerdept",on_delete=SET_NULL,db_column="locker_department",null=True)

class UserManager(BaseUserManager):
    def create_user(self,name,id,departmentname,password=None):
        if not name:
            raise ValueError("USERS MUST HAVE NAME")
        user=self.model(
            name=name,
            id=id,
            department=department.objects.get(deptname=departmentname)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,id,department,password):
        if not name:
            raise ValueError("USERS MUST HAVE NAME")
        user=self.create_user(
            name=name,
            id=id,
            departmentname=department,
            password=password
        )
        user.is_admin=True
        user.save(using=self._db)
        return user

        
class users(AbstractBaseUser):
    name=models.CharField(max_length=10,help_text='이름',null=False)
    id=models.CharField(max_length=8,help_text="학번",primary_key=True,null=False,unique=True)
    lockernum=ForeignKey(lockers,related_name="lockerusing",on_delete=SET_NULL,db_column="lockernum",null=True)
    department=ForeignKey(department,related_name="studentdept",on_delete=SET_NULL,db_column="user_department",null=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    objects=UserManager()
    phone=models.TextField(max_length=20,null=True)
    USERNAME_FIELD='id'
    REQUIRED_FIELDS=['name','department','password']
    def __str__(self):
        return self.name
    def has_perm(self,perm,obj=None):
        if self.is_admin==True and self.is_active==True:
            return True
        else:
            return False
    def has_module_perms(self,app_label):
        if self.is_admin==True and self.is_active==True:
            return True
        else:
            return False
    @property
    def is_staff(self):
        return self.is_admin

class UserSession(models.Model):
    user=models.ForeignKey(users,on_delete=models.CASCADE,editable=False)
    session_key=models.CharField(max_length=100,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore



def kicked_my_other_sessions(sender, request, user, **kwargs):
    for user_session in UserSession.objects.filter(user=user):
        session_key = user_session.session_key
        session = SessionStore(session_key)
        # session.delete()
        session['kicked'] = True
        session.save()
        user_session.delete()

    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key=session_key)

user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')

#user pw initial setting
class usersetting():
    @staticmethod
    def pwthread(dept,result):
        initresult={"result":"","num":0}
        number_process=0
        user_all=users.objects.filter(department=dept)
        for u in user_all:
            if u.is_admin!=True:
                pn=u.phone#전화번호는 010떼고 입력받아야함.
                u.set_password(pn)
                u.save()
                number_process+=1
        result.append(number_process)
        return
    def __init__(self):
        result=list()
        th1=Thread(target=self.pwthread,args=("EIE",result))
        th2=Thread(target=self.pwthread,args=("CS",result))
        th3=Thread(target=self.pwthread,args=("GM",result))
        th4=Thread(target=self.pwthread,args=("SW",result))
        th5=Thread(target=self.pwthread,args=("AIC",result))

        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th1.join()
        th2.join()
        th3.join()
        th4.join()
        th5.join()
        number_process=sum(result)
        if number_process>0:
            print("성공"+str(number_process)+"명")
        else:
            print("실패 혹은 초기화할 유저 없음")