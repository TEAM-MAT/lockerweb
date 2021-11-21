from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey
departments=(('CS','컴퓨터학부'),
    ('GM','글로벌미디어학부'),('EIE','전자정보공학부'),('SW','소프트웨어학부'),
    ('AIC','AI융합학부'))
buildings=(('HN','형남공학관'),('IS','정보과학관'),('CB','문화관'))
class lockers(models.Model):
    lockernum=models.CharField(max_length=10,primary_key=True)#건물앞글자+층+섹터+번호 조합해서 만들기
    written_lockernum=models.IntegerField(default='0')
    floor=models.IntegerField(default=1)
    reserved=models.IntegerField(default=0)#reserved -> 1 unreserved ->0,trigger로 바꿔줘야할듯
    sector=models.CharField(max_length=2,help_text='층별 구역',default='A')
    building=models.CharField(max_length=6,choices=buildings,default='IS')
    department=models.CharField(max_length=4,choices=departments,default="CS")
# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=10,help_text='이름',null=False)
    id=models.CharField(max_length=8,help_text="학번",primary_key=True,null=False)
    pw=models.CharField(max_length=20,null=False)
    lockernum=models.ForeignKey(lockers,related_name="lockerusing",on_delete=SET_NULL,db_column="lockernum",null=True)
    department=models.CharField(max_length=4,choices=departments,default='CS')