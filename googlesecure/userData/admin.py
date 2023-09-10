from django.contrib import admin
from userData.models import UserData,UserEmail,UserPswd
# Register your models here.
@admin.register(UserData)
class AdminUser(admin.ModelAdmin):
    list_display=('email','pswd')

@admin.register(UserEmail)
class AdminUser(admin.ModelAdmin):
    list_display=('email',)


@admin.register(UserPswd)
class AdminUser(admin.ModelAdmin):
    list_display=('pswd',)