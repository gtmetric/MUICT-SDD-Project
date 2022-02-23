from django.db import models
import requests
from django.shortcuts import reverse
from django.utils import timezone, dateformat
from django.core.exceptions import ValidationError


star_systems = eval(requests.get('http://localhost:8080/starsystems').content).get('starSystems')
telescope_locations = eval(requests.get('http://localhost:8080/telescopelocations').content).get('telescopeLocations')

STAR_SYSTEM_CHOICES =  []
for system in star_systems:
    STAR_SYSTEM_CHOICES.append((system, system))
STAR_SYSTEM_CHOICES = tuple(STAR_SYSTEM_CHOICES)

TELESCOPE_LOCATION_CHOICES = []
for location in telescope_locations:
    TELESCOPE_LOCATION_CHOICES.append((location, location))
TELESCOPE_LOCATION_CHOICES = tuple(TELESCOPE_LOCATION_CHOICES)

FILE_TYPE_CHOICES = (('PNG', 'PNG'), ('JPEG', 'JPEG'), ('RAW', 'RAW'))

FILE_QUALITY_CHOICES = (('Low', 'Low'), ('Fine', 'Fine'))

COLOR_TYPE_CHOICES = (('Color mode', 'Color mode'), ('B&W mode', 'B&W mode'))


class SciencePlan(models.Model):
    plan_no = models.IntegerField(primary_key=True)
    creator = models.CharField(max_length=50, default="Creator name")
    submitter = models.CharField(max_length=50, default="Submitter name")
    funding = models.FloatField(default=0.0, verbose_name='Funding (USD)')
    objectives = models.TextField(max_length=255, default='Objectives of this science plan')
    star_system = models.CharField(max_length=255, default='Andromeda', choices=STAR_SYSTEM_CHOICES)
    telescope_location = models.CharField(max_length=255, default='HAWAII', choices=TELESCOPE_LOCATION_CHOICES)
    start_date = models.DateTimeField(default=dateformat.format(timezone.now(), 'Y-d-m H:i:s'))
    end_date = models.DateTimeField(default=dateformat.format(timezone.now(), 'Y-d-m H:i:s'))
    file_type = models.CharField(max_length=255, default='png', choices=FILE_TYPE_CHOICES)
    file_quality = models.CharField(max_length=255, default='fine', choices=FILE_QUALITY_CHOICES)
    color_type = models.CharField(max_length=255, default='color_mode', choices=COLOR_TYPE_CHOICES)
    contrast = models.FloatField(default=0.0)
    brightness = models.FloatField(default=0.0)
    saturation = models.FloatField(default=0.0)
    highlights = models.FloatField(default=0.0)
    exposure = models.FloatField(default=0.0)
    shadows = models.FloatField(default=0.0)
    whites = models.FloatField(default=0.0)
    blacks = models.FloatField(default=0.0)
    luminance = models.FloatField(default=0.0)
    hue = models.FloatField(default=0.0)
    status = models.CharField(max_length=50, blank=True);

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        if self.start_date >= self.end_date or self.start_date < timezone.now() or self.end_date < timezone.now():
            raise ValidationError("The start and end dates are invalid.")
        else:
            super(SciencePlan, self).save(*args, **kwargs)

