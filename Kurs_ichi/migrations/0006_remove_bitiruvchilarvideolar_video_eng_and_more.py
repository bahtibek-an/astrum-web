# Generated by Django 4.2.5 on 2023-09-11 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kurs_ichi', '0005_bitiruvchilar_bitiruvchilarvideolar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitiruvchilarvideolar',
            name='video_eng',
        ),
        migrations.RemoveField(
            model_name='bitiruvchilarvideolar',
            name='video_ru',
        ),
    ]
