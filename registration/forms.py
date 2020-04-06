from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#TEGO NIE POTRZEBUJE!! Jak to usunac, skoro juz bylo w migracji?
#jak chce usunac, wyskakuje mi error:
#ImportError: cannot import name 'UniqueUserForm' from 'registration.forms' (D:\Full stack course\another_try\registration\forms.py)

         #label to bedzie to, co wyswietli sie obok formsa
    # verify_password = forms.CharField(widget=forms.PasswordInput, label="enter your password again") #label to bedzie to, co wyswietli sie obok formsa


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2' #to sa pola z klasy (tabeli) User
        ]
