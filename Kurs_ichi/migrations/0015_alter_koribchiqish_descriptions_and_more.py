# Generated by Django 4.2.6 on 2023-10-23 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kurs_ichi', '0014_remove_koribchiqish_image_koribchiqish_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koribchiqish',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koribchiqish',
            name='descriptions_eng',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koribchiqish',
            name='descriptions_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]