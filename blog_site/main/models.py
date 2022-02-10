from django.db import models
from django.urls import reverse


class News(models.Model):
    header = models.CharField(verbose_name='Заголовок', help_text='Заголовок', max_length=150)
    annotation = models.TextField(verbose_name='Аннотация', help_text='Аннотация')
    full_text = models.TextField(verbose_name='Текст статьи', help_text='Текст статьи')
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='main/static/main/img/news_img/%Y/%m/%d/')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Categories(models.Model):
    category = models.CharField(verbose_name='Категория', help_text='Категория', max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']




