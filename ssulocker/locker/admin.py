from django.contrib import admin
from .models import users
from .models import lockers
admin.site.register(lockers)
class userAdmin(admin.ModelAdmin):
    search_fields=['id']
admin.site.register(users,userAdmin)
# Register your models here.
