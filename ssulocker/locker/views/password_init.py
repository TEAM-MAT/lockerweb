from locker.models import users
from django.contrib.auth.decorators import login_required

@login_required
def pw_init(request):
    return_token=0
    if request.user.is_authenticated:
        if request.user.is_admin==True:
            user_all=users.objects.all()
            for u in user_all:
                if u.is_admin!=True:
                    pn=u.phone[3:]
                    u.set_password(pn)
                    u.save()
            
