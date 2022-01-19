from .models import users
def pw_init(user,phone):
    pn=phone[3:]
    user.set_password(pn)
    user.save()