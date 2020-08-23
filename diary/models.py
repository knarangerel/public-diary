from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def default_descriptors():
    return ["Happy", "Productive", "Energetic", "Active",
            "Silly", "Content", "Motivated", "Joyful",
            "Focused", "Calm", "Average", "Uneventful",
            "Sad", "Depressed", "Anxious", "Numb", "Tired",
            "Irritable", "Lazy", "Insecure", "Cloudy"]


class Diary(models.Model):
    date = models.DateField(auto_now_add=True, primary_key=True)
    caption = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=0,
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])
    adjectives = models.JSONField(default=default_descriptors)

    def __str__(self):
        return str(self.date)
