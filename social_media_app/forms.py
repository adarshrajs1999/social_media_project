from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from social_media_app.models import Social_media_user


class User_register_form(UserCreationForm):
    username = forms.CharField(label = 'username', widget = forms.TextInput(attrs = {'placeholder':'Enter the username'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'placeholder':'Enter the password'}))
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(attrs = {'placeholder':'Confirm the password'}))
    class Meta:
        model = User
        fields = ('username','password1','password2')


class Social_media_user_register_form(forms.ModelForm):
    class Meta:
        model = Social_media_user
        fields = ('__all__')
        exclude = ('user','is_moderator')


