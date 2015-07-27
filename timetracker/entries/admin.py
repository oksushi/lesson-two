from django.contrib import admin

# Register your models here.
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ('project', 'description', 'start', 'stop')
    list_filter = ('project',)
    search_fields = ('project', 'description','client',)

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Project)
admin.site.register(models.Client)
