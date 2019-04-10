from django.shortcuts import render, redirect,HttpResponse
from accounts.forms import RegistrationForm
from django.urls import reverse



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appeng:home')
        else:
            return HttpResponse('You have an error while filling the form , dont forget to set more complex password') 
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'register.html', args)
