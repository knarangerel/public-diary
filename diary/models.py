from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Diary(models.Model):
    date = models.DateField(auto_now_add=True)
    in_couple_words = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=0, validators=[
                                 MaxValueValidator(10), MinValueValidator(1)])
    descriptors = models.JSONField(default="")
    # happy = models.BooleanField(default=False)
    # productive = models.BooleanField(default=False)
    # energetic = models.BooleanField(default=False)
    # active = models.BooleanField(default=False)
    # silly = models.BooleanField(default=False)
    # content = models.BooleanField(default=False)
    # motivated = models.BooleanField(default=False)
    # joyful = models.BooleanField(default=False)
    # focused = models.BooleanField(default=False)
    # calm = models.BooleanField(default=False)
    # average = models.BooleanField(default=False)
    # uneventful = models.BooleanField(default=False)
    # sad = models.BooleanField(default=False)
    # depressed = models.BooleanField(default=False)
    # anxious = models.BooleanField(default=False)
    # numb = models.BooleanField(default=False)
    # tired = models.BooleanField(default=False)
    # irritable = models.BooleanField(default=False)
    # lazy = models.BooleanField(default=False)
    # insecure = models.BooleanField(default=False)
    # cloudy = models.BooleanField(default=False)
