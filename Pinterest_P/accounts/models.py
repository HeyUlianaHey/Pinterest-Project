from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name="Почта")
    username = models.CharField(max_length=150, unique=True, verbose_name="Имя пользователя")
    is_admin = models.BooleanField(default=False, verbose_name="Админ")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "аккаунт"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    photo = models.ImageField(default='profiles/default.png', upload_to='profiles', verbose_name="Фото")
    about = models.TextField(verbose_name="О себе")
    fname = models.CharField(max_length=300, verbose_name="Имя")
    lname = models.CharField(max_length=300, verbose_name="Фамилия")
    pronouns = models.CharField(max_length=100, verbose_name="Цитата")
    website = models.CharField(max_length=100, verbose_name="Веб-сайт")

    class Meta:
        db_table = "профиль"
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f'{self.user.username} Профиль'


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', verbose_name="Подписчик")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', verbose_name="Пользователь")

    class Meta:
        db_table = "подписка"
        verbose_name = "Подписку"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'{self.follower} подписка на {self.following}'








