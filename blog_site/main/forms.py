from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    class Meta():
        model = News
        fields = ['header', 'annotation', 'full_text', 'image', 'category']
        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            'annotation': forms.Textarea(attrs={'class': 'form-control'}),
            'full_text': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }