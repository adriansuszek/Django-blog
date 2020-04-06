from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration_form(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() #zapisywanie do bazy
            user_name = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user_name)
            return redirect('/login') #przekierowanie do jakiegos htmla z blog.view
        # else:
        #     messages.error()

    context = {'form': form}
    return render(request, 'register_form.html', context) # w TEJ LINIJCE!



def login_form(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #checking if user is in DB:
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/') #przekierowanie do jakiegos htmla z blog.view TU TRZEBA POPRAWIC
        else:
            messages.info(request, 'Username OR password is incorrect.')

    context= {}
    return render(request, 'login_form.html', context) # w TEJ LINIJCE!


def logout_form(request):
    logout(request)
    return redirect('/login')
