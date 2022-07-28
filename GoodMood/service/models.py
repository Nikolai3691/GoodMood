from django.db import models
from django.urls import reverse


class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название услуги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Цена услуги')
    write_up = models.TextField(blank=True, verbose_name='Описание услуги')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    worker = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Работник')
    sub_cat = models.ForeignKey('service.Subcategory', on_delete=models.PROTECT, verbose_name='Подкатегория')
    duration = models.BigIntegerField(default=0, verbose_name='Время процедуры')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services', kwargs={'services_slug': self.slug})

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
        ordering = ['id']

    ordering = ['title', 'price']


class Subcategory(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию услуг'
        verbose_name_plural = 'Категории услуг'
        ordering = ['id']

    ordering = ['title']

