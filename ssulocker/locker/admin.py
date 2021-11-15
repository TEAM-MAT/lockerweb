from django.contrib import admin
from .models import personalinfo
from .models import locker
admin.site.register(locker)
class userAdmin(admin.ModelAdmin):
    search_fields=['user']
admin.site.register(personalinfo,userAdmin)
# Register your models here.
