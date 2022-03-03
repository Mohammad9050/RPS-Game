from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# from Home.models import PostModel
from Home.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'incls'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'incls'}))
    password2 = forms.CharField(label='Re - enter password', widget=forms.PasswordInput(attrs={'class': 'incls'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'incls'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'incls'}))


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = PostModel
#         fields = ('text', 'age', 'detail')
#
#     def clean(self):
#         cleaned_data = super(PostForm, self).clean()
#         age = cleaned_data['age']
#         if age < 18:
#             self.add_error(None, ValidationError('you should older than 18'))
#         return cleaned_data


class SearchForm(forms.Form):
    query = forms.CharField(max_length=50)


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    password = None


