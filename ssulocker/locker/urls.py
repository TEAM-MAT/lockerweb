from django.urls import path

from . import views
#from django.contrib.auth import views as auth_views
from .reserve import reserve_process as rsp
app_name='locker'
urlpatterns = [
    #path('', views.index, name='index'),
    path('lockerlist',views.lockerlist,name='lockerlist'),
    path('login',views.index,name='login'),
    path('registeration_popup',views.registpop,name="rpop"),
    path('',views.index,name='maintologin')
]