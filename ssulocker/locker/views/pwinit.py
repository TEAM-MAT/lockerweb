from locker.models import users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from locker.middleware import init_pw
@login_required
def pw_init(request):
     if request.user.is_authenticated:
        if request.user.is_admin==True:
            user_all=users.objects.all()
            initiation=init_pw(user_all)
            return render(request,'locker/pwresult.html',initiation)      
        else:
             return redirect('/locker/login')
     else:
         return redirect('/locker/login')
