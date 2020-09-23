from django.contrib import admin
from .models import Trip,Like,Comment,Contact

class TripAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)

admin.site.register(Trip, TripAdmin)
admin.site.register(Like)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact)
