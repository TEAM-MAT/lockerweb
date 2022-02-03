from locker.models import users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

@login_required
def pw_init(request):
     number_process=0
     result_test=""
     initresult={"result":result_test,"num":number_process}
     if request.user.is_authenticated:
         if request.user.is_admin==True:
             user_all=users.objects.all()
             for u in user_all:
                 if u.is_admin!=True:
                     pn=u.phone#전화번호는 010떼고 입력받아야함.
                     u.set_password(pn)
                     u.save()
                     number_process+=1
             if number_process>0:
                 initresult["result"]="성공"
             else:
                 initresult["result"]="실패"
             initresult["num"]=number_process
             return render(request,'locker/pwresult.html',initresult)      
         else:
             return redirect('/locker/login')
     else:
         return redirect('/locker/login')
