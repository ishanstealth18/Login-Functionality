from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Register_Table
from email_confirmation import forms
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def login(request):
    return render(request, 'login_page.html')


def signup(request):
    user_data = Register_Table.objects.all().values()
    context = {
        'user_data': user_data
    }
    initial_form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        #user_data = Register_Table()
        #user_data.firstname = request.POST.get('firstname')
        #user_data.lastname = request.POST.get('lastname')
        #user_data.save()
        #messages.success(request, 'You have been registered successfully!!')
        #return redirect('')

        if form.is_valid():
            form.save()
            messages.success(request, 'You have been registered successfully!!')
            send_mail("Successful registration", "Hello, you are now registered!!", "ishanstealth18@yahoo.co.in"
                      , ["ishan.stealth@gmail.com"])
            return redirect("http://127.0.0.1:8000/")
            #return render(request, 'signup.html', {'form': initial_form})
    else:
        form = forms.SignupForm()
        return render(request, 'signup.html', {'form': form})
