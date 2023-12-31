# Generated by Django 4.2.4 on 2023-09-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy_Sahifa', '0003_remove_whyastrum_short_descriptions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyAstrumInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('short_descriptions', models.CharField(blank=True, max_length=500)),
                ('title_ru', models.CharField(blank=True, max_length=256)),
                ('short_descriptions_ru', models.CharField(blank=True, max_length=500)),
                ('title_eng', models.CharField(blank=True, max_length=256)),
                ('short_descriptions_eng', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
