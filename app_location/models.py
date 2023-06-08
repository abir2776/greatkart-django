from django.db import models
from django.urls import reverse

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def get_url(self):
        return reverse('products_by_location',args=[self.slug])

    def __str__(self):
        return self.location
