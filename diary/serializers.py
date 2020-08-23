from datetime import date
from rest_framework import serializers
from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('date', 'in_couple_words', 'rating', 'descriptors')

    def create(self, validated_data):
        diary, _ = Diary.objects.update_or_create(
            date=date.today(),
            defaults={'in_couple_words': validated_data.get('in_couple_words', None),
                      'rating': validated_data.get('rating', None),
                      'descriptors': validated_data.get('descriptors', None)})
        return diary
