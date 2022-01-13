from django.contrib.auth.decorators import login_required
from models import users
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.shortcuts import render,redirect
@login_required(login_url='locker:login')
def pwchange(request):
    if request.method=="POST":
        #form data받아서 처리
        form=PasswordChangeForm(request.user,request.POST)
        

    elif request.method=="GET":
        #form 전송
        form=PasswordChangeForm(request.user)
    return render(request,'locker/pwchange.html',{"form":form})
def pwclogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('locker/pwchange')
        else:
            return redirect('locker/pwchange_login')
#def cleaned_password()