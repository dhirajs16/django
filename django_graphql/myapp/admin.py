from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'city']