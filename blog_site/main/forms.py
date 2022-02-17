from django import forms
from .models import *

class NewsForm(forms.Form):
    header = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={"class": "form-control",
                                                                                              "rows": 5,}))
    annotation = forms.CharField(label='Аннотация', widget=forms.Textarea(attrs={"class": "form-control",
                                                                                 "rows": 5,}))
    full_text = forms.CharField(label='Текст статьи', widget=forms.Textarea(attrs={"class": "form-control",
                                                                                   "rows": 5,}))
    image = forms.ImageField(label='Фото', required=False, widget=forms.FileInput(attrs={"class": "form-control",}))
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', required=False, empty_label=None, widget=forms.Select(attrs={"class": "form-control",}))
