from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget



class NewsForm(forms.ModelForm):
    category = forms.ModelChoiceField(empty_label=None, queryset=Categories.objects.all())

    class Meta():
        model = News
        fields = ['header', 'annotation', 'full_text', 'image', 'category']
        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            'annotation': forms.Textarea(attrs={'class': 'form-control'}),
            'full_text': forms.Textarea(),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'},),}
