from django.db import models

        
class CamerasCat(models.Model):
        title = models.CharField(max_length=50, blank=True)
        location = models.CharField(max_length=50, blank=True)
        url = models.URLField(blank=True)
        lat = models.FloatField(blank=True, null=True)
        lon = models.FloatField(blank=True, null=True)
        date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
        date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
        is_removed = models.BooleanField(default=False)
        
     
        def __str__(self):
            return self.title



