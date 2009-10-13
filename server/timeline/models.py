from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=222)
    start = models.DateTimeField()
    end   = models.DateTimeField()
    dur   = models.BooleanField()

    ordering = ['-start']

    def __unicode__(self):
        return str(self.start) + ' ' + self.title
    
