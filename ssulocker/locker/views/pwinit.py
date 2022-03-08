from locker.models import users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from locker.middleware import init_pw
@login_required
def pw_init(request):
     number_process=0
     result_test=""
     initresult={"result":result_test,"num":number_process}
     if request.user.is_authenticated:
        if request.user.is_admin==True:
            user_all=users.objects.all()
            pw_init(user_all,initresult)
            return render(request,'locker/pwresult.html',initresult)      
        else:
             return redirect('/locker/login')
     else:
         return redirect('/locker/login')
