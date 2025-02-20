from django.contrib import admin
from .models import Property, Request  # Ensure to import the Request model

# Register your models here.
admin.site.register(Property)
admin.site.register(Request)  # Register the Request model