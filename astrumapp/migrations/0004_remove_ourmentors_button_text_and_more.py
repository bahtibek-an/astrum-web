# Generated by Django 4.2.3 on 2023-09-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astrumapp', '0003_mainheader_image_eng_mainheader_image_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourmentors',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='ourmentors',
            name='button_text_eng',
        ),
        migrations.RemoveField(
            model_name='ourmentors',
            name='button_text_ru',
        ),
    ]