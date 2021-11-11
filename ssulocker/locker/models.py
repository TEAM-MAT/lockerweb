from django.db import models
from django.db.models.fields.related import ForeignKey
class personalinfo(models.Model):
    name=models.CharField(max_length=10,help_text='이름',null=False)
    id=models.CharField(max_length=8,help_text="학번",primary_key=True,null=False)
    pw=models.CharField(max_length=20,null=False)
    lockernum=models.IntegerField()
    department=models.Choices(('cs','컴퓨터학부'),
    ('GM','글로벌미디어학부'),('EIE','전자정보공학부'),('SW','소프트웨어학부'),
    ('AIC','AI융합학부'))
class locker(models.Model):
    lockernum=models.IntegerField(primary_key=True)
    floor=models.IntegerField()
# Create your models here.
