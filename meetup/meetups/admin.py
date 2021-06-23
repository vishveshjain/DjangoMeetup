from django.contrib import admin
from django.db import models
from .models import Location, Meetup, Organizer, Participant

# Register your models here.
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Organizer)

@admin.register(Meetup)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'organizer')
    list_filter = ('location','organizer')
    prepopulated_fields = {'slug': ('title', )}


