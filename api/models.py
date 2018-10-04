from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
# Create your models here.
class messdaten(models.Model):

    offenname=models.CharField(max_length=120, null=True, blank=True)
    O2 = models.CharField(max_length=120, null=True, blank=True)
    CO = models.CharField(max_length=120, null=True, blank=True)
    CO2 = models.CharField(max_length=120, null=True, blank=True)
    NO = models.CharField(max_length=120, null=True, blank=True)
    NO2 = models.CharField(max_length=120, null=True, blank=True)
    SO2 = models.CharField(max_length=120, null=True, blank=True)
    NOX = models.CharField(max_length=120, null=True, blank=True)
    ETA = models.CharField(max_length=120, null=True, blank=True)
    Lamda = models.CharField(max_length=120, null=True, blank=True)
    Losses = models.CharField(max_length=120, null=True, blank=True)
    Air_temperatur = models.CharField(max_length=120, null=True, blank=True)
    Gas_temp = models.CharField(max_length=120, null=True, blank=True)
    Airpressure = models.CharField(max_length=140, null=True, blank=True)

    #class Meta:

        #ordering = ('created',)