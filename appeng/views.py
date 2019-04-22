from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from appeng.models import User_answer, Words, User_anwer_QuerySet
from django.contrib.auth.decorators import login_required


def home(request):
    win_score = User_anwer_QuerySet.course_final_score(current_user=request.user)
    if request.user.is_authenticated:
        try:
            user_answers = User_anwer_QuerySet.get_user_answer(
                current_user=request.user
            )
            words = User_anwer_QuerySet.get_user_not_answer(current_user=request.user)
            user_score = User_anwer_QuerySet.score_user(current_user=request.user)
            if user_score >= win_score:
                messages = "YOU WIN"
                return render(request, "appeng/home.html")
            args = {
                "words": words,
                "win_score": win_score,
                "user_score": user_score,
                "user_answers": user_answers,
            }

            return render(request, "appeng/home.html", args)
        except User_answer.DoesNotExist:
            return render(request, "appeng/home.html")
    return render(request, "appeng/home.html")


@login_required
def set_course(request):
    current_user = request.user
    User_answer.objects.get_or_create(current_user=current_user, answer=False)
    return redirect("appeng:home")


def change_answer(request, operation, pk):
    user_anser = Words.objects.get(pk=pk)
    if operation == "add":
        User_answer.know_word(request.user, user_anser)
    elif operation == "remove":
        User_answer.dont_know_word(request.user, user_anser)
    return redirect("appeng:home")
