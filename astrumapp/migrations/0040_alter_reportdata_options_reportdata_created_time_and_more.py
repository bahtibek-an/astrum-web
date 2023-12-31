# Generated by Django 4.2.2 on 2023-10-06 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('astrumapp', '0039_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportdata',
            options={'ordering': ('created_time',), 'verbose_name': 'Report Data', 'verbose_name_plural': 'Report Data'},
        ),
        migrations.AddField(
            model_name='reportdata',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportdata',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
