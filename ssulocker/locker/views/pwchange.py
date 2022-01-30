from django.contrib.auth.decorators import login_required
from locker.models import users
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render,redirect
#@login_required(login_url='locker:pwclogin')
def pwchangePop(request):
    return render(request,'locker/pwchange_login.html')
def pwchange(request):
    if request.method=="POST":
        #form data받아서 처리
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"비밀번호가 변경되었습니다.")
            return redirect('locker:login')
        else:
            #messages.error("에러 발생")
            return redirect('locker:pwchangePop')

    elif request.method=="GET":
        # form 전송
        form= PasswordChangeForm(request.user)
        return render(request,'locker/pwchange.html',{"form":form})
def pwclogin(request):
    error=0
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('locker:pwchange')
        else:
            error=1
            return render(request,'locker/pwchange_login.html',{"error":error})
        
#def cleaned_password()