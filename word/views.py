from django.shortcuts import render, redirect
from django.urls import reverse
from word.words import kor, eng


def get_quiz(request):
    # localhost: 8000/word?index=0&correct=0

    if request.method == "GET":  # GET: url 치고 enter
        index = int(request.GET.get("index", 0))  # request.GET: url
        correct = int(request.GET.get("correct", 0))

        action = ""
        if index == 4:
            # reverse: 이름으로 url 찾는 함수
            action += reverse("result")

        # context: 변수 역할
        context = {
            "index": index,
            "quiz": eng[index],
            "action": action,
            "correct": correct
        }
        return render(request, "word/index.html", context)

    if request.method == "POST":  # POST: 정답제출
        index = int(request.POST.get("index"))
        before_correct = int(request.POST.get("correct"))
        answer = request.POST.get("answer")

        correct = before_correct
        if answer == kor[index]:
            correct += 1

        next_url = "quiz" if int(index) < 4 else "result"

        # redirect: POST 후 돌아갈 url 지정
        # localhost:8000/word?index={}&correct={}
        # localhost:8000/word/result
        return redirect(
            reverse(next_url) +
            f"?index={index + 1}&correct={correct}"
        )


def get_result(request):
    if request.method == "POST":
        index = int(request.POST.get("index"))
        correct = int(request.POST.get("correct"))
        answer = request.POST.get("answer")

        result = correct
        if answer == kor[index]:
            result += 1

        context = {
            "result": result
        }
        return render(request, "word/result.html", context)
