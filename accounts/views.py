from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registred")
            return redirect("appeng:home")
        else:
            messages.error(
                request,
                "You have an error while filling the form , dont forget to set more complex password",
            )
            return redirect("accounts:register")
    else:
        form = RegistrationForm()
        args = {"form": form}
        return render(request, "accounts/register.html", args)
