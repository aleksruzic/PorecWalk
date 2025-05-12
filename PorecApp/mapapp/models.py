from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def google_maps_url(self):
        return f"https://www.google.com/maps/dir/?api=1&destination={self.latitude},{self.longitude}"
