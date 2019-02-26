"""
Forms
"""
from django import forms

"""
Class Register Form
"""
class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
