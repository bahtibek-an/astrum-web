# Generated by Django 4.2.5 on 2023-09-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biz_haqimizda', '0005_alter_photo_img1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='karyera',
            name='img1',
            field=models.ImageField(blank=True, upload_to='about_us/'),
        ),
        migrations.AddField(
            model_name='karyera',
            name='img2',
            field=models.ImageField(blank=True, upload_to='about_us/'),
        ),
        migrations.AddField(
            model_name='karyera',
            name='img3',
            field=models.ImageField(blank=True, upload_to='about_us/'),
        ),
        migrations.AddField(
            model_name='karyera',
            name='img4',
            field=models.ImageField(blank=True, upload_to='about_us/'),
        ),
        migrations.AddField(
            model_name='karyera',
            name='img5',
            field=models.ImageField(blank=True, upload_to='about_us/'),
        ),
        migrations.AddField(
            model_name='karyera',
            name='img6',
            field=models.ImageField(blank=True, upload_to='about_us/'),
        ),
    ]
