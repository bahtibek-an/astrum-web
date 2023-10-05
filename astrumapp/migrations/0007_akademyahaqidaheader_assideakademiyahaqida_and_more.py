# Generated by Django 4.2.3 on 2023-09-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrumapp', '0006_remove_footer_category1_remove_footer_category1_eng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkademyaHaqidaHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('descriptions', models.CharField(max_length=300)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('image4', models.ImageField(upload_to='')),
                ('image5', models.ImageField(upload_to='')),
                ('image6', models.ImageField(upload_to='')),
                ('image7', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(blank=True, max_length=50)),
                ('descriptions_ru', models.CharField(max_length=300)),
                ('image1_ru', models.ImageField(upload_to='')),
                ('image2_ru', models.ImageField(upload_to='')),
                ('image3_ru', models.ImageField(upload_to='')),
                ('image4_ru', models.ImageField(upload_to='')),
                ('image5_ru', models.ImageField(upload_to='')),
                ('image6_ru', models.ImageField(upload_to='')),
                ('image7_ru', models.ImageField(upload_to='')),
                ('title_eng', models.CharField(blank=True, max_length=50)),
                ('descriptions_eng', models.CharField(max_length=300)),
                ('image1_eng', models.ImageField(upload_to='')),
                ('image2_eng', models.ImageField(upload_to='')),
                ('image3_eng', models.ImageField(upload_to='')),
                ('image4_eng', models.ImageField(upload_to='')),
                ('image5_eng', models.ImageField(upload_to='')),
                ('image6_eng', models.ImageField(upload_to='')),
                ('image7_eng', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AssideAkademiyaHaqida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('image_ru', models.ImageField(upload_to='')),
                ('title_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
                ('image_eng', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AssideKurslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('image_ru', models.ImageField(upload_to='')),
                ('title_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
                ('image_eng', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AssideMashgulotKurslari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('image_ru', models.ImageField(upload_to='')),
                ('title_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
                ('image_eng', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AssideOqituvchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('title_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('title_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='AssideQulaylik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('image_ru', models.ImageField(upload_to='')),
                ('title_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
                ('image_eng', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AssideTalimTizimi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('image4', models.ImageField(upload_to='')),
                ('image5', models.ImageField(upload_to='')),
                ('image6', models.ImageField(upload_to='')),
                ('image7', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('image1_ru', models.ImageField(upload_to='')),
                ('image2_ru', models.ImageField(upload_to='')),
                ('image3_ru', models.ImageField(upload_to='')),
                ('image4_ru', models.ImageField(upload_to='')),
                ('image5_ru', models.ImageField(upload_to='')),
                ('image6_ru', models.ImageField(upload_to='')),
                ('image7_ru', models.ImageField(upload_to='')),
                ('title_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
                ('image1_eng', models.ImageField(upload_to='')),
                ('image2_eng', models.ImageField(upload_to='')),
                ('image3_eng', models.ImageField(upload_to='')),
                ('image4_eng', models.ImageField(upload_to='')),
                ('image5_eng', models.ImageField(upload_to='')),
                ('image6_eng', models.ImageField(upload_to='')),
                ('image7_eng', models.ImageField(upload_to='')),
            ],
        ),
    ]