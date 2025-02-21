from django.contrib import admin
from .models import Property, Request, UserMessage  # Ensure to import the Request model

# Register your models here.
admin.site.register(Property)
admin.site.register(Request)  


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Add more fields as needed
    search_fields = ('name', 'email', 'message')  # Enable searching by these fields