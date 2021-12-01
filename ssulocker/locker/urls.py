from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
app_name='locker'
urlpatterns = [
    #path('', views.index, name='index'),
    path('lockerlist',views.lockerlist,name='lockerlist'),
    path('login',auth_views.LoginView.as_view(template_name='locker/index.html'),name='login')
]