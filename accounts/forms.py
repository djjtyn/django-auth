from django import forms

class UserLoginForm(forms.Form):
    """Form to be used for logging users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)