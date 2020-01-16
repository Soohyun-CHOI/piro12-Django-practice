from django.shortcuts import render


def get_quiz(request):
    context = {}
    return render(request, "word/index.html", context)