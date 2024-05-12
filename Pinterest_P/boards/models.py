from django.db import models

from accounts.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_user', verbose_name="Пользователь")
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    pins = models.ManyToManyField('pins.Pin', related_name='pins', blank=True, verbose_name="Пин")
    cover = models.ImageField(upload_to='boards', default='boards/default.png', verbose_name="Обложка")
    is_private = models.BooleanField(default=False, verbose_name="Приватность")
    description = models.CharField(max_length=250, blank=True, verbose_name="Описание")

    class Meta:
        db_table = "доска"
        verbose_name = "Доску"
        verbose_name_plural = "Доски"

    def __str__(self):
        return self.title
