from django.contrib import admin
from .models import Ticket, Message, Categorie
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(Ticket)
admin.site.register(Categorie)
admin.site.register(Message)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
