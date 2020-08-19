from django.urls import path
from . import views

urlpatterns = [
    path('api/diary/', views.DiaryListCreate.as_view()),
]
