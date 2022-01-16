from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
departments=(('CS','컴퓨터학부'),
    ('GM','글로벌미디어학부'),('EIE','전자정보공학부'),('SW','소프트웨어학부'),
    ('AIC','AI융합학부'))
buildings=(('HN','형남공학관'),('IS','정보과학관'),('CB','문화관'))
class department(models.Model):
    deptname=models.CharField(max_length=6,choices=departments,primary_key=True)
    time=models.DateTimeField()#예약시작날짜 

    def getdepttime(self):
        return self.time

class lockers(models.Model):
    lockernum=models.CharField(max_length=10,primary_key=True)#건물앞글자+층+섹터+번호 조합해서 만들기
    written_lockernum=models.IntegerField(default='0')
    floor=models.IntegerField(default=1)
    reserved=models.IntegerField(default=0)#reserved -> 1 unreserved ->0,trigger로 바꿔줘야할듯
    sector=models.CharField(max_length=2,help_text='층별 구역',default='A')
    building=models.CharField(max_length=6,choices=buildings,default='IS')
    department=ForeignKey(department,related_name="lockerdept",on_delete=SET_NULL,db_column="locker_department",null=True)
class UserManager(BaseUserManager):
    def create_user(self,name,id,department,password=None):
        if not name:
            raise ValueError("USERS MUST HAVE NAME")
        user=self.model(
            name=name,
            id=id,
            department=department
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
            department=department,
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
    phone=models.CharField(max_length=12,help_text="전화번호")
    objects=UserManager()
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
