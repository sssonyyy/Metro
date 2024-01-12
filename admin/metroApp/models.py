from django.db import models
from django.urls import reverse


class Metro(models.Model):

    id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=30)
    depo = models.CharField(max_length=30)
    exit1 = models.CharField(max_length=30)
    exit2 = models.CharField(max_length=30)
    plan1 = models.CharField(max_length=30)
    plan2 = models.CharField(max_length=30)
    brak = models.CharField(max_length=30)
    zader = models.CharField(max_length=30)
    snizh_dkr_kr = models.CharField(max_length=30)
    snizhskor = models.CharField(max_length=30)
    pereklpotu = models.CharField(max_length=30)
    itogo = models.CharField(max_length=30)
    itogoproc = models.CharField(max_length=30)
    flightwithoutplan = models.CharField(max_length=30)
    srskor = models.CharField(max_length=30)
    srskorplan = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('spravka', kwargs={'slug': self.slug})

class Drivers(models.Model):
    id_driver = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tram_number = models.CharField(max_length=30)





# Create your models here.
