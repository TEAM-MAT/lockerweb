from django.contrib.auth.decorators import login_required
from models import users
from django.contrib.auth.forms import PasswordChangeForm
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
    
#def cleaned_password()