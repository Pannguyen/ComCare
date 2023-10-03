from django.contrib import admin

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'createur', 'date_creation', 'data_cloture', 'etat')