from django.contrib import admin
from .models import Artist, Track, Dance
# Register your models here.
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(Dance)
