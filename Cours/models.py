from django.db import models


# Create your models here.

class Kurslar(models.Model):
    title = models.CharField(max_length=250, blank=True)

    title_ru = models.CharField(max_length=250, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=20, blank=True)
    image = models.ImageField(blank=True)
    data = models.CharField(max_length=156, blank=True)
    short_descriptions = models.CharField(max_length=256, blank=True)
    short_descriptions_big = models.CharField(max_length=500, blank=True)
    duration = models.CharField(max_length=256, blank=True)

    title_ru = models.CharField(max_length=20, blank=True)
    data_ru = models.CharField(max_length=156, blank=True)
    short_descriptions_ru = models.CharField(max_length=256, blank=True)
    short_descriptions_big_ru = models.CharField(max_length=500, blank=True)
    duration_ru = models.CharField(max_length=256, blank=True)

    title_eng = models.CharField(max_length=20, blank=True)
    data_eng = models.CharField(max_length=156, blank=True)
    short_descriptions_eng = models.CharField(max_length=256, blank=True)
    short_descriptions_big_eng = models.CharField(max_length=500, blank=True)
    duration_eng = models.CharField(max_length=256, blank=True)
    is_main = models.BooleanField(default=False)

    

    def __str__(self):
        return self.title


