# Generated by Django 3.1 on 2020-08-23 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='descriptors',
            new_name='adjectives',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='in_couple_words',
            new_name='caption',
        ),
    ]
