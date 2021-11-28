from django.contrib import admin

from locker.forms import UserCreationForm,UserChangeForm
from .models import users
from .models import lockers
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
admin.site.register(lockers)
class userAdmin(admin.ModelAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    list_display=('id','name','lockernum','department','is_admin')
    list_filter=('is_admin','department',)
    fieldsets=(
        (None,{'fields':('id','name')}),
        ('Locker',{'fields':('lockernum',)}),
        ('Permissions',{'fields':('is_admin',)}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','date_of_birth','password1','password2'),
        }),
    )
    search_fields=('id','name','department')
    ordering=('id',)
    filter_horizontal=()
admin.site.register(users,userAdmin)
admin.site.unregister(Group)
# Register your models here.
