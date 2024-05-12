# Generated by Django 4.1.4 on 2024-05-12 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0001_initial'),
        ('boards', '0003_board_description_board_is_private'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'Доску', 'verbose_name_plural': 'Доски'},
        ),
        migrations.AlterField(
            model_name='board',
            name='cover',
            field=models.ImageField(default='boards/default.png', upload_to='boards', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.CharField(blank=True, max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='board',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Приватность'),
        ),
        migrations.AlterField(
            model_name='board',
            name='pins',
            field=models.ManyToManyField(blank=True, related_name='pins', to='pins.pin', verbose_name='Пин'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='board',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterModelTable(
            name='board',
            table='доска',
        ),
    ]
