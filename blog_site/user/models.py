from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(verbose_name='Дата рождения', auto_now_add=False)
    profession = models.CharField(verbose_name='Профессия', help_text='Профессия', max_length=150)
    about = models.TextField(verbose_name='О себе', help_text='О себе')
    work_experience = models.ManyToManyField('WorkExperiance')
    education = models.ManyToManyField('Education')
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='user/static/user/img/users_photo/%Y/%m/%d/')
    summary = models.FileField(verbose_name='Резюме', blank=True, upload_to='user/static/user/docs/%Y/%m/%d/')
    social_links = models.ManyToManyField('SocialLinks')
    Phone = models.CharField(verbose_name='Телефон', help_text='Телефон', max_length=15)
    skills = models.TextField(verbose_name='Навыки', help_text='Навыки')
    pass

class WorkExperiance(models.Model):
    company = models.CharField(verbose_name='Компания', help_text='Компания', max_length=150)
    position = models.CharField(verbose_name='Должность', help_text='Должность', max_length=150)
    responsibilities = models.TextField(verbose_name='Обязанности', help_text='Обязанности')
    date_of_employment = models.DateField(verbose_name='Дата приема на работу', auto_now_add=False)
    date_of_dismissal = models.DateField(verbose_name='Дата увольнения', auto_now_add=False)
    pass


class Education(models.Model):
    place_of_study = models.CharField(verbose_name='Место учебы', help_text='Место учебы', max_length=150)
    degree = models.CharField(verbose_name='Степень', help_text='Степень', max_length=150)
    date_of_admission = models.DateField(verbose_name='Дата поступления', auto_now_add=False)
    date_of_graduation = models.DateField(verbose_name='Дата окончания', auto_now_add=False)
    pass


class SocialLinks(models.Model):
    social_link_name = models.CharField(verbose_name='Название социальной сети', help_text='Название социальной сети', max_length=150)
    link_value = models.CharField(verbose_name='Ссылка', help_text='Ссылка', max_length=150)
    pass
