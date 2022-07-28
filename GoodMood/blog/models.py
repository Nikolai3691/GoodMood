from django.db import models
from django.urls import reverse


class Publications(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('public', kwargs={'public_slug': self.slug})

    class Meta:
        verbose_name = 'Публикацию'
        verbose_name_plural = 'Публикации'
        ordering = ['id']

    ordering = ['title', 'time_create']


class Comment(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    person_comment = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, verbose_name='Клиент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('add_comment ', kwargs={'add_comment': self.slug})

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']

    ordering = ['title', 'time_create']


class Records(models.Model):
    title = models.CharField(max_length=255, verbose_name='Услуга')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    record_closed = models.DateTimeField(verbose_name='Запись закрыта')
    record_open = models.DateTimeField(verbose_name='Запись открыта')
    person_record = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Клиент')
    service = models.ForeignKey('service.Services', on_delete=models.CASCADE, verbose_name='Услуга')

    # def save(self, *args, **kwargs):
    #     kwargs['record_closed'] = kwargs.get('record_open').timestamp() + kwargs['service'].duration
    #     super().save(args, kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('records', kwargs={'records': self.slug})

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['id']
