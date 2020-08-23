from datetime import date
from rest_framework import serializers
from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('date', 'caption', 'rating', 'adjectives')

    def create(self, validated_data):
        diary, _ = Diary.objects.update_or_create(
            date=date.today(),
            defaults={'caption': validated_data.get('caption', None),
                      'rating': validated_data.get('rating', None),
                      'adjectives': validated_data.get('adjectives', None)})
        return diary
