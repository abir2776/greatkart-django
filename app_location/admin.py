from django.contrib import admin
from .models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('location',)}
    list_display = ('location','slug')


admin.site.register(Location,LocationAdmin)