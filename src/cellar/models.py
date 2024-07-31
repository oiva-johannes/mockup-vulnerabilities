from django.db import models

from django.contrib.auth.models import User

class Wines(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    vintage = models.IntegerField()
    score = models.IntegerField()
    #type = models.CharField(max_length=120)
    #grape = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

#class Prices(models.Model):
    #id = models.BigAutoField(primary_key=True)
    #wine_id = models.ForeignKey(Wines, on_delete=models.CASCADE)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    #price_date = models.DateField()

class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    wine_id = models.ForeignKey(Wines, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    #location = models.CharField(max_length=120)
    # TODO: add images
    # TODO: href column
