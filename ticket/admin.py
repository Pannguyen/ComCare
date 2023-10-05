from django.contrib import admin
from .models import Ticket
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
#admin.py
admin.site.register(Ticket)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)