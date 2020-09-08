from django.contrib import admin
from .models import Trip,Like

class TripAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Trip, TripAdmin)
admin.site.register(Like)
