from rest_framework import generics
from .models import Diary
from .serializers import DiarySerializer


class DiaryView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class SingleDiaryView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'date'
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
