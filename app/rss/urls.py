from django.urls import path

from rss import views

urlpatterns = [
    path('', views.IndexView.as_view()),
]
