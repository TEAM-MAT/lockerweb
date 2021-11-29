from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
app_name='locker'
urlpatterns = [
    path('', views.index, name='index'),
    path('lockerlist',views.lockerlist,name='lockerlist'),
    path('login',views.login,name='login')
]