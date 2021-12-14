from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from .reserve import reserve_process as rsp
app_name='locker'
urlpatterns = [
    #path('', views.index, name='index'),
    path('lockerlist',views.lockerlist,name='lockerlist'),
    path('login',auth_views.LoginView.as_view(template_name='locker/index.html'),name='login'),
    path('registeration_popup',views.registpop,name="rpop")
]