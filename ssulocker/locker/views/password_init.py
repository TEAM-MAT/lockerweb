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
                    pn=u.phone[3:]
                    u.set_password(pn)
                    u.save()
                    number_process+=1
            if number_process>0:
                result_test="성공"
            else:
                result_test="실패"
            render(request,'locker/pwresult.html',initresult)      
        else:
            redirect('locker/login')
    else:
        redirect('locker/login')

            
