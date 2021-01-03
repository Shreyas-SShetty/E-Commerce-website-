from django.conf import settings
from django.db import models
from django.utils import timezone

class Item(models.Model) :
    name = models.CharField(max_length=100, null=False)
    cost = models.IntegerField(null=False)
    images = models.ImageField(upload_to='images/', null=False)
    seller = models.CharField(max_length=200, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

class Buyer(models.Model) :
    name = models.CharField(max_length=100, null=False)
    wallet = models.IntegerField(default=100)

    def __str__(self):
        return str(self.name)
