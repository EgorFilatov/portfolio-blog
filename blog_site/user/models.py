from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(verbose_name='Дата рождения', auto_now_add=False, blank=True)
    profession = models.CharField(verbose_name='Профессия', help_text='Профессия', max_length=150, blank=True)
    about = models.TextField(verbose_name='О себе', help_text='О себе', blank=True)
    work_experience = models.ManyToManyField('WorkExperiance', blank=True)
    education = models.ManyToManyField('Education', blank=True)
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='user/static/user/img/users_photo/%Y/%m/%d/')
    summary = models.FileField(verbose_name='Резюме', blank=True, upload_to='user/static/user/docs/%Y/%m/%d/')
    social_links = models.ManyToManyField('SocialLinks', blank=True)
    Phone = models.CharField(verbose_name='Телефон', help_text='Телефон', max_length=15, blank=True)
    skills = models.TextField(verbose_name='Навыки', help_text='Навыки', blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class WorkExperiance(models.Model):
    company = models.CharField(verbose_name='Компания', help_text='Компания', max_length=150)
    position = models.CharField(verbose_name='Должность', help_text='Должность', max_length=150)
    responsibilities = models.TextField(verbose_name='Обязанности', help_text='Обязанности', blank=True)
    date_of_employment = models.DateField(verbose_name='Дата приема на работу', auto_now_add=False, blank=True)
    date_of_dismissal = models.DateField(verbose_name='Дата увольнения', auto_now_add=False, blank=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Education(models.Model):
    place_of_study = models.CharField(verbose_name='Место учебы', help_text='Место учебы', max_length=150)
    degree = models.CharField(verbose_name='Степень', help_text='Степень', max_length=150, blank=True)
    date_of_admission = models.DateField(verbose_name='Дата поступления', auto_now_add=False, blank=True)
    date_of_graduation = models.DateField(verbose_name='Дата окончания', auto_now_add=False, blank=True)

    def __str__(self):
        return self.place_of_study

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class SocialLinks(models.Model):
    social_link_name = models.CharField(verbose_name='Название социальной сети', help_text='Название социальной сети', max_length=150)
    link_value = models.CharField(verbose_name='Ссылка', help_text='Ссылка', max_length=150)

    def __str__(self):
        return self.social_link_name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
