# Generated by Django 4.2.3 on 2023-09-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrumapp', '0007_akademyahaqidaheader_assideakademiyahaqida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='descriptions',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image1_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image1_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image2_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image2_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image3_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image3_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image4_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image4_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image5_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image5_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image6',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image6_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image6_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image7',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image7_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='image7_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='akademyahaqidaheader',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='descriptions_eng',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='image_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='image_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assideakademiyahaqida',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='descriptions_eng',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='image_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='image_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidekurslar',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='descriptions_eng',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='image_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='image_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidemashgulotkurslari',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assideoqituvchilar',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assideoqituvchilar',
            name='descriptions_eng',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assideoqituvchilar',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assideoqituvchilar',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assideoqituvchilar',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assideoqituvchilar',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='descriptions_eng',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='image_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='image_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidequlaylik',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='descriptions_eng',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image1_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image1_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image2_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image2_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image3_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image3_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image4_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image4_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image5_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image5_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image6',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image6_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image6_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image7',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image7_eng',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='image7_ru',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='title_eng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='assidetalimtizimi',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
