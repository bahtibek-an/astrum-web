# Generated by Django 4.2.5 on 2023-10-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy_Sahifa', '0020_theles_name_eng_theles_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theles',
            name='name_eng',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='theles',
            name='short_descriptions_eng',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='theles',
            name='title_eng',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]