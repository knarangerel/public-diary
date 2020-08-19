from rest_framework import generics
from .models import Diary
from .serializers import DiarySerializer


class DiaryListCreate(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
