from django.db import models
from django.urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField


class News(models.Model):
    header = models.CharField(verbose_name='Заголовок', max_length=150)
    annotation = models.TextField(verbose_name='Аннотация')
    full_text = RichTextField(blank=True, null=True, verbose_name='Текст статьи')
    #full_text = models.TextField(blank=True, null=True, verbose_name='Текст статьи')
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='media/img/news_img/%Y/%m/%d/')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Categories(models.Model):
    category = models.CharField(verbose_name='Категория', help_text='Категория', max_length=50)

    def get_absolute_url(self):
        return reverse_lazy('categories', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']




