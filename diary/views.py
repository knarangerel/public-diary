import datetime
from django.http import Http404
from rest_framework import generics
from .models import Diary
from .serializers import DiarySerializer


class DiaryView(generics.ListCreateAPIView):
    serializer_class = DiarySerializer

    def get_queryset(self):
        diary = Diary.objects.filter(date=datetime.date.today())
        if not diary:
            raise Http404
        return diary


class PastDiaryView(generics.ListCreateAPIView):
    serializer_class = DiarySerializer

    def get_queryset(self):
        num_of_days = 1
        diary = Diary.objects.filter(
            date=datetime.date.today() - datetime.timedelta(days=num_of_days))
        while not diary:
            num_of_days += 1
            diary = Diary.objects.filter(
                date=datetime.date.today() - datetime.timedelta(days=num_of_days))
        return diary
