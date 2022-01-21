from django.urls import path

from . import views
#from django.contrib.auth import views as auth_views
from .reserve import reserve_process as rsp
app_name='locker'
urlpatterns = [
    #path('', views.index, name='index'),
    path('lockerlist',views.lockerlist,name='lockerlist'),
    path('login',views.index,name='login'),
    path('',views.index,name='maintologin'),
    path('logout',views.logout,name='logout'),
    path('reserve',views.reserve,name='reserve'),
    path('reservePop',views.reservePop,name='reservePop'),
    path('cancelPop',views.cancelPop,name='cancelPop'),
    path('cancel',views.cancel,name='cancel'),
]