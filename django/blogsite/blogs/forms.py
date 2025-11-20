from django import forms
from .models import Blog,Users

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'
    widgets={
        'password':forms.PasswordInput()
    }


