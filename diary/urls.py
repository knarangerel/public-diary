from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('diary/', views.DiaryView.as_view()),
    url(r'^(?P<date>\d{4}-\d{2}-\d{2})/$', views.SingleDiaryView.as_view()),
]
