from django.db import models
from mimetypes import guess_type

from accounts.models import User
from boards.models import Board


class Pin(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pin_user', verbose_name="Пользователь"
    )
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='boards', verbose_name="Доска"
    )
    file = models.FileField(upload_to='pins', verbose_name="Файл")
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    link = models.CharField(max_length=250, verbose_name="Ссылка")
    description = models.TextField(verbose_name="Описание")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        db_table = "пин"
        verbose_name = "Пин"
        verbose_name_plural = "Пины"

    def __str__(self):
        return self.title

    def get_type(self):
        file_type = guess_type(self.file.url, strict=True)[0]
        # file_type might be ('video/mp4', None) or ('image/jpeg..etc', None)
        if 'video' in file_type:
            return 'video'
        elif 'image' in file_type:
            return 'image'


class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name='comments', verbose_name="Пин")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_comments', verbose_name="Пользователь")
    text = models.CharField(max_length=250, verbose_name="Содержание")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        db_table = "комментарий"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.user} комментирует {self.text}'
