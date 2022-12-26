# Generated by Django 4.1.4 on 2022-12-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_cover_board_pins'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
