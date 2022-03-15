from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'about')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),}


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'})),


class CustomUserForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'about', 'photo', 'date_of_birth', 'profession', 'skills', 'summary', 'Phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.FileInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

