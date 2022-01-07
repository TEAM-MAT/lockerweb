from django.contrib import admin

from locker.forms import UserCreationForm,UserChangeForm
from .models import users,lockers,department
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from locker.forms import lockeraddForm#lockerchangeForm
class userAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    list_display=('id','name','lockernum','department','lockernum','is_admin')
    list_filter=('is_admin','department','lockernum')
    fieldsets=(
        (None,{'fields':('id','name','department','password')}),
        ('Permissions',{'fields':('is_admin',)}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('id','name','password1','password2','department','is_admin'),
        }),
    )
    search_fields=('id','name','department')
    ordering=('id',)
    filter_horizontal=()
class lockerAdmin(admin.ModelAdmin):
    add_form=lockeraddForm
    list_display=('lockernum','building','department','reserved')
    list_filter=('lockernum','building','department','reserved')
    fieldsets=(
        (None,{'fields':('lockernum','building','department','reserved')}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('building','written_lockernum','floor','sector','department','reserved')
        }),
    )
    search_fields=('lockernum','building','sector','reserved')
    ordering=('lockernum',)
    filter_horizontal=()
admin.site.register(users,userAdmin)
#admin.site.register(lockers,lockerAdmin)
admin.site.register(lockers)
admin.site.unregister(Group)
admin.site.register(department)
# Register your models here.
