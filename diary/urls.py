from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.DiaryView.as_view()),
    path('lastavailable/', views.PastDiaryView.as_view()),
]
