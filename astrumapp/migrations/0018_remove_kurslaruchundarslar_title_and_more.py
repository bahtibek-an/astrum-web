# Generated by Django 4.2.3 on 2023-09-08 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astrumapp', '0017_alter_kurslaruchundarslar_descriptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurslaruchundarslar',
            name='title',
        ),
        migrations.RemoveField(
            model_name='kurslaruchundarslar',
            name='title_eng',
        ),
        migrations.RemoveField(
            model_name='kurslaruchundarslar',
            name='title_ru',
        ),
    ]