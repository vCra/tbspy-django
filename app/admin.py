from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Price)
admin.site.register(Ticket)
admin.site.register(UserProfile)
admin.site.register(Tour)
admin.site.register(Artist)