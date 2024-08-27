from django import forms
from .models import Account
# from account import forms

class NewAccount(forms.Form):
    id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=200, required=True ,widget=forms.PasswordInput,)
    email = forms.EmailField(max_length=245,required=True)
    image = forms.ImageField(required=False)

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=245, required=True)
    password = forms.CharField(max_length=200,required=True,widget=forms.PasswordInput)


