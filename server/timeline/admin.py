from server.timeline.models import Event 
from django.contrib import admin 
 
class EventAdmin(admin.ModelAdmin):
    fields = [ 'title', 'dur', 'start', 'end', 'desc']
    list_display = ('dur', 'start', 'end', 'title')
    list_filter = ['start', 'end', 'dur']
    search_fields = ['title']
    date_hierarchy = 'start'
    list_display_links = ['start','end','title']


admin.site.register(Event, EventAdmin)
