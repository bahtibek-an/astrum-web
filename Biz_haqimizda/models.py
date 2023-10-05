from django.db import models


# Create your models here.


class Karyera(models.Model):
    title = models.CharField(max_length=250, blank=True)
    short_descriptions = models.CharField(max_length=500, blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    short_descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    short_descriptions_eng = models.CharField(max_length=500, blank=True)

    image1 = models.ImageField(upload_to='about_us/', blank=True)
    image2 = models.ImageField(upload_to='about_us/', blank=True)
    image3 = models.ImageField(upload_to='about_us/', blank=True)
    image4 = models.ImageField(upload_to='about_us/', blank=True)
    image5 = models.ImageField(upload_to='about_us/', blank=True)

    def __str__(self):
        return self.title


class Vakansiya(models.Model):
    data = models.CharField(max_length=20, blank=True)
    image = models.ImageField(blank=True)
    occupation = models.CharField(max_length=250, blank=True)
    short_descriptions = models.CharField(max_length=256, blank=True)
    prise = models.CharField(max_length=100, blank=True)
    button_text = models.CharField(max_length=20, blank=True)

    data_ru = models.CharField(max_length=20, blank=True)
    occupation_ru = models.CharField(max_length=250, blank=True)
    short_descriptions_ru = models.CharField(max_length=256, blank=True)
    prise_ru = models.CharField(max_length=100, blank=True)
    button_text_ru = models.CharField(max_length=20, blank=True)

    data_eng = models.CharField(max_length=20, blank=True)
    occupation_eng = models.CharField(max_length=250, blank=True)
    short_descriptions_eng = models.CharField(max_length=256, blank=True)
    prise_eng = models.CharField(max_length=100, blank=True)
    button_text_eng = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.data
