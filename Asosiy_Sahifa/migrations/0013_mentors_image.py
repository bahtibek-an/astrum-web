# Generated by Django 4.2.4 on 2023-09-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy_Sahifa', '0012_remove_mentors_image_remove_mentors_image_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentors',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
