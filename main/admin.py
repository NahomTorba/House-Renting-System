from django.contrib import admin

# Register your models here.

from .models import Property, Booking

admin.site.register(Property)
admin.site.register(Booking)
