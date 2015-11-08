from models import *
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
	model = Blog


