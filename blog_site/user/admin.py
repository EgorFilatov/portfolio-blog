from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'username', 'email',]
    list_display_links = ['first_name', 'username',]
    search_fields = ['date_of_birth', 'profession', 'about', 'work_experience', 'education', 'photo', 'social_links', 'Phone', 'skills',]

admin.site.register(CustomUser, CustomUserAdmin)


class WorkExperianceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'date_of_employment', 'date_of_dismissal',]

admin.site.register(WorkExperiance, WorkExperianceAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['place_of_study', 'degree', 'date_of_admission', 'date_of_graduation',]

admin.site.register(Education, EducationAdmin)


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['social_link_name',]
admin.site.register(SocialLinks, SocialLinksAdmin)

