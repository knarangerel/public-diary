from django.db import models


class Diary(models.Model):
    date = models.DateField(auto_now_add=True)
    in_couple_words = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=0)

    HAPPY = '001'
    PRODUCTIVE = '002'
    ENERGETIC = '003'
    ACTIVE = '004'
    SILLY = '005'
    CONTENT = '006'
    MOTIVATED = '007'
    JOYFUL = '008'
    FOCUSED = '009'
    CALM = '101'
    AVERAGE = '102'
    UNEVENTFUL = '103'
    SAD = '201'
    DEPRESSED = '202'
    ANXIOUS = '203'
    NUMB = '204'
    TIRED = '205'
    IRRITABLE = '206'
    LAZY = '207'
    INSECURE = '208'
    CLOUDY = '209'
    MOOD_DESCRIPTORS = [
        (HAPPY, 'Happy'),
        (PRODUCTIVE, 'Productive'),
        (ENERGETIC, 'Energetic'),
        (ACTIVE, 'Active'),
        (SILLY, 'Silly'),
        (CONTENT, 'Content'),
        (MOTIVATED, 'Motivated'),
        (JOYFUL, 'Joyful'),
        (FOCUSED, 'Focused'),
        (CALM, 'Calm'),
        (AVERAGE, 'Average'),
        (UNEVENTFUL, 'Uneventful'),
        (SAD, 'Sad'),
        (DEPRESSED, 'Depressed'),
        (ANXIOUS, 'Anxious'),
        (NUMB, 'Numb'),
        (TIRED, 'Tired'),
        (IRRITABLE, 'Irritable'),
        (LAZY, 'Lazy'),
        (INSECURE, 'Insecure'),
        (CLOUDY, 'Cloudy'),
    ]
    descriptors = models.CharField(
        max_length=3,
        choices=MOOD_DESCRIPTORS,
    )
