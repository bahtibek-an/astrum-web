# Generated by Django 4.2.5 on 2023-09-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugungiTolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oylik_tolov_chegirma', models.CharField(max_length=100)),
                ('skidka', models.CharField(max_length=100)),
                ('narx_oyiga', models.CharField(max_length=100)),
                ('kurs_name', models.CharField(max_length=100)),
                ('kurs_narx', models.CharField(max_length=100)),
                ('skidka_text', models.CharField(max_length=100)),
                ('skidka_narx', models.CharField(max_length=100)),
                ('jami_skidka', models.CharField(max_length=100)),
                ('jami_narx', models.CharField(max_length=100)),
                ('oylik_tolov_chegirma_ru', models.CharField(max_length=100)),
                ('skidka_ru', models.CharField(max_length=100)),
                ('narx_oyiga_ru', models.CharField(max_length=100)),
                ('kurs_name_ru', models.CharField(max_length=100)),
                ('kurs_narx_ru', models.CharField(max_length=100)),
                ('skidka_text_ru', models.CharField(max_length=100)),
                ('skidka_narx_ru', models.CharField(max_length=100)),
                ('jami_skidka_ru', models.CharField(max_length=100)),
                ('jami_narx_ru', models.CharField(max_length=100)),
                ('oylik_tolov_chegirma_eng', models.CharField(max_length=100)),
                ('skidka_eng', models.CharField(max_length=100)),
                ('narx_oyiga_eng', models.CharField(max_length=100)),
                ('kurs_name_eng', models.CharField(max_length=100)),
                ('kurs_narx_eng', models.CharField(max_length=100)),
                ('skidka_text_eng', models.CharField(max_length=100)),
                ('skidka_narx_eng', models.CharField(max_length=100)),
                ('jami_skidka_eng', models.CharField(max_length=100)),
                ('jami_narx_eng', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BugungiTolovQulayligi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_ru', models.CharField(max_length=500)),
                ('title_eng', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='KursJadvali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=156)),
                ('name', models.CharField(max_length=156)),
                ('descriptions', models.CharField(max_length=156)),
                ('title_ru', models.CharField(max_length=156)),
                ('name_ru', models.CharField(max_length=156)),
                ('descriptions_ru', models.CharField(max_length=156)),
                ('title_eng', models.CharField(max_length=156)),
                ('name_eng', models.CharField(max_length=156)),
                ('descriptions_eng', models.CharField(max_length=156)),
            ],
        ),
        migrations.CreateModel(
            name='KurslarUchunDarslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=500)),
                ('image1', models.ImageField(upload_to='kurs_ichi/')),
                ('image2', models.ImageField(upload_to='kurs_ichi/')),
                ('image3', models.ImageField(upload_to='kurs_ichi/')),
                ('image4', models.ImageField(upload_to='kurs_ichi/')),
                ('image5', models.ImageField(upload_to='kurs_ichi/')),
                ('title_ru', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=100)),
                ('descriptions_ru', models.CharField(max_length=250)),
                ('title_eng', models.CharField(max_length=50)),
                ('name_eng', models.CharField(max_length=100)),
                ('descriptions_eng', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='KursPLan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs_name', models.CharField(max_length=156)),
                ('data', models.CharField(max_length=500)),
                ('oqish_davomiligi', models.CharField(max_length=156)),
                ('name_lastname', models.CharField(max_length=156)),
                ('image', models.ImageField(upload_to='kurs_ichi/')),
                ('sohasi', models.CharField(max_length=156)),
                ('kurs_name_ru', models.CharField(max_length=156)),
                ('data_ru', models.CharField(max_length=500)),
                ('oqish_davomiligi_ru', models.CharField(max_length=156)),
                ('name_lastname_ru', models.CharField(max_length=156)),
                ('sohasi_ru', models.CharField(max_length=156)),
                ('kurs_name_eng', models.CharField(max_length=156)),
                ('data_eng', models.CharField(max_length=500)),
                ('oqish_davomiligi_eng', models.CharField(max_length=156)),
                ('name_lastname_eng', models.CharField(max_length=156)),
                ('sohasi_eng', models.CharField(max_length=156)),
            ],
        ),
        migrations.CreateModel(
            name='Narxlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=156)),
                ('name', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=500)),
                ('title_ru', models.CharField(max_length=156)),
                ('name_ru', models.CharField(max_length=250)),
                ('descriptions_ru', models.CharField(max_length=500)),
                ('title_eng', models.CharField(max_length=156)),
                ('name_eng', models.CharField(max_length=250)),
                ('descriptions_eng', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OylikTolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oyiga', models.CharField(max_length=100)),
                ('besh_x_oylik_tolovlar', models.CharField(max_length=100)),
                ('jami_narx', models.CharField(max_length=100)),
                ('oyiga_ru', models.CharField(max_length=100)),
                ('besh_x_oylik_tolovlar_ru', models.CharField(max_length=100)),
                ('jami_narx_ru', models.CharField(max_length=100)),
                ('oyiga_eng', models.CharField(max_length=100)),
                ('besh_x_oylik_tolovlar_eng', models.CharField(max_length=100)),
                ('jami_narx_eng', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OylikTolovQulayligi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_ru', models.CharField(max_length=500)),
                ('title_eng', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Savollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=156)),
                ('name', models.CharField(max_length=156)),
                ('descriptions', models.CharField(max_length=156)),
                ('title_ru', models.CharField(max_length=156)),
                ('name_ru', models.CharField(max_length=156)),
                ('descriptions_ru', models.CharField(max_length=156)),
                ('title_eng', models.CharField(max_length=156)),
                ('name_eng', models.CharField(max_length=156)),
                ('descriptions_eng', models.CharField(max_length=156)),
            ],
        ),
        migrations.CreateModel(
            name='SavollarJavob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.CharField(max_length=1000)),
                ('title_ru', models.CharField(max_length=200)),
                ('descriptions_ru', models.CharField(max_length=1000)),
                ('title_eng', models.CharField(max_length=200)),
                ('descriptions_eng', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TreningDasturi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=250)),
                ('title_ru', models.CharField(max_length=100)),
                ('name_ru', models.CharField(max_length=250)),
                ('title_eng', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TreningDasturiAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=250)),
                ('title_ru', models.CharField(max_length=100)),
                ('descriptions_ru', models.CharField(max_length=250)),
                ('title_eng', models.CharField(max_length=100)),
                ('descriptions_eng', models.CharField(max_length=250)),
            ],
        ),
    ]
