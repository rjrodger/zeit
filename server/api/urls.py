from django.conf.urls.defaults import *
from piston.resource import Resource
from server.api.handlers import TimelineHandler

timeline_handler = Resource(TimelineHandler)

urlpatterns = patterns('',
   url(r'^timeline', timeline_handler),
)

