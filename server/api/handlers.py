from piston.handler import AnonymousBaseHandler
from server.timeline.models import Event
import simplejson
from django.http import *
from datetime import datetime


class TimelineHandler(AnonymousBaseHandler):
   allowed_methods = ('GET',)

   def read(self, request):
       events = []
       for event in Event.objects.all():
           color = "#6666ff"
           if event.title.startswith("DEV IR"):
              color = "#ff3333"
           elif event.title.startswith("TEST IR"):
              color = "#cc9900"
           elif event.title.startswith("LIVE IR"):
              color = "#33aa33"

           events.append( {"start":event.start.strftime("%a %b %d %Y %H:%M:%S GMT-0000"), "description":event.desc, "color":color,
                           "end":event.end.strftime("%a %b %d %Y %H:%M:%S GMT-0000"), "durationEvent":event.dur, "title":event.title} )

       outstr = simplejson.dumps( {"events":events} )
       
       res = HttpResponse(outstr);
       return res

