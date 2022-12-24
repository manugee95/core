from django.contrib import admin
from main.models import *

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'area', 'name', 'maryland', 'virginia', 'columbia', 'servicess']
    list_editable = ['maryland', 'virginia', 'columbia', 'servicess']

class HomeProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'appname']

admin.site.register(HomeProfile)
admin.site.register(Career)
admin.site.register(PositionApplied)
admin.site.register(State)
admin.site.register(StateApplied)
admin.site.register(Time)
admin.site.register(Location)
admin.site.register(Service, ServiceAdmin)