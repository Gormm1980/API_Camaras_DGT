from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class TrafficCamera(TimeStampedModel, SoftDeletableModel):
        title = models.CharField(max_length=50, blank=True)
        url = models.URLField(blank=True)
        lat = models.IntegerField(blank=True, null=True)
        lon = models.IntegerField(blank=True, null=True)
        date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
        date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
        is_removed = models.BooleanField(default=False)
        
        def __str__(self):
            return self.title

        
class Location(models.Model):
        name = models.CharField(max_length=255, db_index=True)
        traffic_cameras = models.ForeignKey(TrafficCamera, on_delete=models.CASCADE)
        
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs, ) 
            return None
        
        def __str__(self):
            return self.name




