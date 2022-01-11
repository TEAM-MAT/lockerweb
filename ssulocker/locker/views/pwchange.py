from django.contrib.auth.decorators import login_required
@login_required(login_url='locker:login')
def pwchange(request):
    if request.method=="POST":
        