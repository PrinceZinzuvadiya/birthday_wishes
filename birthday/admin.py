from django.contrib import admin
from .models import wishes

class adminModel(admin.ModelAdmin):
    list_display= ('wish', 'to')
admin.site.register(wishes, adminModel)