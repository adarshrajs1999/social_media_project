from django import forms
from django.contrib.auth.forms import UserCreationForm
from social_media_app.models import User_model

class User_creation_form(UserCreationForm):
    username = forms.CharField(label = 'Username', widget = forms.TextInput(attrs = {'placeholder':'Enter your username'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'placeholder':'Enter your password'}))
    password2 = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput(attrs = {'placeholder':'Confirm your password'}))
    
    class Meta:
        model = User_model
        fields = ('username', 'password1', 'password1')



