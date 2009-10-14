from server.timeline.models import Event 
from django.contrib import admin 
from django import forms


class EventModelForm( forms.ModelForm ):
    desc = forms.CharField( label="Description", widget=forms.Textarea, initial=" " )
    class Meta:
        model = Event

 
class EventAdmin(admin.ModelAdmin):
    form = EventModelForm
    fields = [ 'title', 'dur', 'start', 'end', 'desc']
    list_display = ('dur', 'start', 'end', 'title')
    list_filter = ['start', 'end', 'dur']
    search_fields = ['title']
    date_hierarchy = 'start'
    list_display_links = ['start','end','title']


admin.site.register(Event, EventAdmin)
