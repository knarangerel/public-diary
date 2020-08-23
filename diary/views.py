from datetime import date
from rest_framework import generics
from .models import Diary
from .serializers import DiarySerializer


class DiaryView(generics.ListCreateAPIView):
    queryset = Diary.objects.filter(date=date.today())
    serializer_class = DiarySerializer
