# Generated by Django 4.2.4 on 2023-09-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy_Sahifa', '0005_newsheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=156)),
                ('title', models.CharField(blank=True, max_length=156)),
                ('short_descriptions', models.CharField(blank=True, max_length=256)),
                ('button_text', models.CharField(blank=True, max_length=10)),
                ('name_ru', models.CharField(blank=True, max_length=156)),
                ('title_ru', models.CharField(blank=True, max_length=156)),
                ('short_descriptions_ru', models.CharField(blank=True, max_length=256)),
                ('button_text_ru', models.CharField(blank=True, max_length=10)),
                ('name_eng', models.CharField(blank=True, max_length=156)),
                ('title_eng', models.CharField(blank=True, max_length=156)),
                ('short_descriptions_eng', models.CharField(blank=True, max_length=256)),
                ('button_text_eng', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
