# Generated by Django 4.2.6 on 2023-10-23 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cours', '0006_courses_is_main'),
        ('Kurs_ichi', '0017_alter_savollar1_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.TextField()),
                ('course_structure', models.TextField()),
                ('about_season', models.CharField(max_length=400)),
                ('title_ru', models.CharField(max_length=200)),
                ('descriptions_ru', models.TextField()),
                ('course_structure_ru', models.TextField()),
                ('about_season_ru', models.CharField(max_length=400)),
                ('title_en', models.CharField(max_length=200)),
                ('descriptions_en', models.TextField()),
                ('course_structure_en', models.TextField()),
                ('about_season_en', models.CharField(max_length=400)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_programs', to='Cours.courses')),
            ],
            options={
                'verbose_name': 'Учебная программа',
                'verbose_name_plural': 'Учебные программы',
            },
        ),
        migrations.CreateModel(
            name='QuestionAndAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(max_length=400)),
                ('training_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kurs_ichi.trainingprogram')),
            ],
            options={
                'verbose_name': 'Вопрос и ответ',
                'verbose_name_plural': 'Вопросы и ответы',
            },
        ),
    ]
