from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'category', 'created_at',]
    list_display_links = ['id', 'header',]
    search_fields = ['header', 'category', 'annotation', 'full_text',]

admin.site.register(News, NewsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'category',]

admin.site.register(Categories, CategoriesAdmin)