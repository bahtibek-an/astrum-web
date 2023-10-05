# Generated by Django 4.2.5 on 2023-09-11 21:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kurs_ichi', '0004_alter_koribchiqish_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitiruvchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=500)),
                ('title_ru', models.CharField(max_length=100)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('title_eng', models.CharField(max_length=100)),
                ('descriptions_eng', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BitiruvchilarVideolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lastname', models.CharField(max_length=256)),
                ('skill', models.CharField(max_length=500)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('name_lastname_ru', models.CharField(max_length=256)),
                ('skill_ru', models.CharField(max_length=500)),
                ('video_ru', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('name_lastname_eng', models.CharField(max_length=256)),
                ('skill_eng', models.CharField(max_length=500)),
                ('video_eng', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
            ],
        ),
    ]