# Generated by Django 4.2.3 on 2023-09-11 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cours', '0004_remove_kurslar_image_eng_remove_kurslar_image_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurslar',
            name='image',
        ),
    ]