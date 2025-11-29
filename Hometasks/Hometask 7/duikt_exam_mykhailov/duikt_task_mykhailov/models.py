from django.db import models

class CarsBrand(models.Model):
    BRAND_NAME = models.CharField(max_length=100)
    BRAND_COUNTRY = models.CharField(max_length=100)
    BRAND_RATING = models.IntegerField()

    def __str__(self):
        return self.BRAND_NAME


class CarsInfo(models.Model):
    CAR_NAME = models.CharField(max_length=100)
    CAR_MODEL = models.CharField(max_length=100)
    CAR_PRICE = models.FloatField()
    CAR_BRAND = models.ForeignKey(CarsBrand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.CAR_NAME} {self.CAR_MODEL}"
