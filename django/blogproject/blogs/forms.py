from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'



# class BlogForm(forms.Form):
#     title=forms.CharField(required=True,
#         error_messages={
#             'required':'Title is required'
#         })
#     rating=forms.IntegerField(max_value=5)


