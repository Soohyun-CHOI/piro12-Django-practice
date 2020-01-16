from django.urls import path
from word.views import get_quiz


urlpatterns = [
    path("", get_quiz, name="quiz"),
]
