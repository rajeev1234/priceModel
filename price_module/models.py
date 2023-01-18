from django.db import models

# Create your models here.

TITLE_CHOICES = (
    (1, ("Distance Base Price")),
    (2, ("Distance Additional Price")),
)
class PriceModule(models.Model):
    title = models.IntegerField(choices=TITLE_CHOICES, default=1)  
    distance_in_meters = models.IntegerField(default=0)
    price = models.FloatField(blank=True, null =True)
    tmf_under_hour = models.FloatField(default=1)
    tmf_for_two_hour = models.FloatField(default=1.25)
    tmf_for_three_hour = models.FloatField(default=2.2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.id}"