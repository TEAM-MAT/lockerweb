from django.urls import path
from django.contrib.auth import views as v
app_name='login'
urlpatterns=[
    path('login/',v.LoginView.as_view(template_name='login/loginview.html'),name='login')
]