from django.db import models


# Create your models here.

class AkademyaHaqidaHeader(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=300, blank=True)

    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    image7 = models.ImageField(blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=300, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    descriptions_eng = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    

class AssideAkademiyaHaqida(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    descriptions_eng = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class AssideTalimTizimi(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=500, blank=True)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    image7 = models.ImageField(blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class AssideQulaylik(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    descriptions_eng = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class AssideKurslar(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    descriptions_eng = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class AssideOqituvchilar(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=500, blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    descriptions_eng = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class AssideMashgulotKurslari(models.Model):
    title = models.CharField(max_length=250, blank=True)
    descriptions = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(blank=True)

    title_ru = models.CharField(max_length=250, blank=True)
    descriptions_ru = models.CharField(max_length=1000, blank=True)

    title_eng = models.CharField(max_length=250, blank=True)
    descriptions_eng = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
