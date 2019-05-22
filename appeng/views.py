from django.shortcuts import render, redirect
from appeng.models import User_anwer_QuerySet as Qs
from appeng.models import User_answer, Words
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    current_user = request.user
    win_score = Qs.course_final_score(current_user)
    if request.user.is_authenticated:
        try:
            user_answers = Qs.get_user_answer(current_user)
            words = Qs.get_user_not_answer(current_user)
            user_score = User_answer.objects.get(current_user=current_user).user_score
            if user_score >= win_score:
                a = User_answer.objects.get(current_user=current_user).words.clear()
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
    messages.success(request, "Here we go")
    return redirect("appeng:home")


def change_answer(request, operation, pk):
    user_anser = Words.objects.get(pk=pk)
    if operation == "add":
        User_answer.know_word(request.user, user_anser)
    elif operation == "remove":
        User_answer.dont_know_word(request.user, user_anser)
    return redirect("appeng:home")
