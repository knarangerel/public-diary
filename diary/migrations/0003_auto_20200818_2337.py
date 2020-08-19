# Generated by Django 3.1 on 2020-08-18 23:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20200818_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='active',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='anxious',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='average',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='calm',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='cloudy',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='content',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='depressed',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='energetic',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='focused',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='happy',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='insecure',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='irritable',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='joyful',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='lazy',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='motivated',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='numb',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='productive',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='sad',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='silly',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='tired',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='uneventful',
        ),
        migrations.AddField(
            model_name='diary',
            name='descriptors',
            field=models.JSONField(default=''),
        ),
        migrations.AlterField(
            model_name='diary',
            name='rating',
            field=models.DecimalField(decimal_places=0, max_digits=2, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]