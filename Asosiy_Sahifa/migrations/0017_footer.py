# Generated by Django 4.2.4 on 2023-09-09 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy_Sahifa', '0016_locatsiainfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motto', models.CharField(blank=True, max_length=156)),
                ('short_descriptions', models.CharField(blank=True, max_length=256)),
                ('motto_ru', models.CharField(blank=True, max_length=156)),
                ('short_descriptions_ru', models.CharField(blank=True, max_length=256)),
                ('motto_eng', models.CharField(blank=True, max_length=156)),
                ('short_descriptions_eng', models.CharField(blank=True, max_length=256)),
            ],
        ),
    ]