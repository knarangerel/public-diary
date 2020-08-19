from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Diary(models.Model):
    date = models.DateField(auto_now_add=True)
    in_couple_words = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=0,
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])
    descriptors = models.JSONField(default=list)
