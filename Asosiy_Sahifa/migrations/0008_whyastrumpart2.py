# Generated by Django 4.2.4 on 2023-09-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy_Sahifa', '0007_remove_coursinfo_button_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyAstrumPart2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=156)),
                ('title', models.CharField(blank=True, max_length=156)),
                ('name_ru', models.CharField(blank=True, max_length=156)),
                ('title_ru', models.CharField(blank=True, max_length=156)),
                ('name_eng', models.CharField(blank=True, max_length=156)),
                ('title_eng', models.CharField(blank=True, max_length=156)),
            ],
        ),
    ]