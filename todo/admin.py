from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','descriptions', 'data' ,'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title','descriptions')
    list_editable = ('done',)
    list_filter = ('done',)

admin.site.register(Todo, TodoAdmin)
