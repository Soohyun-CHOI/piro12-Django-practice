from django.urls import path
from word.views import get_quiz, get_result

urlpatterns = [
    path("", get_quiz, name="quiz"),
    path("result/", get_result, name="result")
]
