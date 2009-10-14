from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=222)
    start = models.DateTimeField(default=datetime.today())
    end   = models.DateTimeField(default=datetime.today())
    dur   = models.BooleanField("Time Period")
    desc  = models.CharField("Description", max_length=2222, blank=True, null=True, default="aaa")

    ordering = ['-start']

    def __unicode__(self):
        return str(self.start) + ' ' + self.title
    
