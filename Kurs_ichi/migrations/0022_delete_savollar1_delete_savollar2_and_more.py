# Generated by Django 4.2.6 on 2023-10-25 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cours', '0006_courses_is_main'),
        ('Kurs_ichi', '0021_remove_trainingprogram_about_season_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Savollar1',
        ),
        migrations.DeleteModel(
            name='Savollar2',
        ),
        migrations.DeleteModel(
            name='SavollarJavob1',
        ),
        migrations.DeleteModel(
            name='SavollarJavob2',
        ),
        migrations.AddField(
            model_name='koribchiqish',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_views', to='Cours.courses'),
        ),
    ]
