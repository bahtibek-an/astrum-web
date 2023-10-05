from django.db import models


class NewsHeader(models.Model):
    title = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=255)

    title_ru = models.CharField(max_length=256, blank=True)
    link_ru = models.CharField(max_length=255)

    title_eng = models.CharField(max_length=256, blank=True)
    link_eng = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MainHeader(models.Model):
    title = models.CharField(max_length=50, blank=True)

    title_ru = models.CharField(max_length=50, blank=True)

    title_eng = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    img = models.ImageField(blank=True)
    name = models.CharField(max_length=156, blank=True)
    photo_name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    descriptions = models.CharField(max_length=10000, blank=True)
    image = models.ImageField(blank=True)

    name_ru = models.CharField(max_length=156, blank=True)
    photo_name_ru = models.CharField(max_length=50, blank=True)
    title_ru = models.CharField(max_length=50, blank=True)
    descriptions_ru = models.CharField(max_length=10000, blank=True)

    name_eng = models.CharField(max_length=156, blank=True)
    photo_name_eng = models.CharField(max_length=50, blank=True)
    title_eng = models.CharField(max_length=50, blank=True)
    descriptions_eng = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.name


class WhyAstrum(models.Model):
    title = models.CharField(max_length=156, blank=True)
    name = models.CharField(max_length=156, blank=True)

    title_ru = models.CharField(max_length=156, blank=True)
    name_ru = models.CharField(max_length=156, blank=True)

    title_eng = models.CharField(max_length=156, blank=True)
    name_eng = models.CharField(max_length=156, blank=True)

    def __str__(self):
        return self.title


class WhyAstrumInfo(models.Model):
    title = models.CharField(max_length=256, blank=True)
    short_descriptions = models.CharField(max_length=500, blank=True)

    title_ru = models.CharField(max_length=256, blank=True)
    short_descriptions_ru = models.CharField(max_length=500, blank=True)

    title_eng = models.CharField(max_length=256, blank=True)
    short_descriptions_eng = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class CoursInfo(models.Model):
    name = models.CharField(max_length=156, blank=True)
    title = models.CharField(max_length=156, blank=True)
    short_descriptions = models.CharField(max_length=256, blank=True)

    name_ru = models.CharField(max_length=156, blank=True)
    title_ru = models.CharField(max_length=156, blank=True)
    short_descriptions_ru = models.CharField(max_length=256, blank=True)

    name_eng = models.CharField(max_length=156, blank=True)
    title_eng = models.CharField(max_length=156, blank=True)
    short_descriptions_eng = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class WhyAstrumPart2(models.Model):
    name = models.CharField(max_length=156, blank=True)
    title = models.CharField(max_length=156, blank=True)

    name_ru = models.CharField(max_length=156, blank=True)
    title_ru = models.CharField(max_length=156, blank=True)

    name_eng = models.CharField(max_length=156, blank=True)
    title_eng = models.CharField(max_length=156, blank=True)

    def __str__(self):
        return self.name


class WhyAstrumInfo2(models.Model):
    name = models.CharField(max_length=156, blank=True)
    title = models.CharField(max_length=156, blank=True)
    short_descriptions = models.CharField(max_length=256, blank=True)

    name_ru = models.CharField(max_length=156, blank=True)
    title_ru = models.CharField(max_length=156, blank=True)
    short_descriptions_ru = models.CharField(max_length=256, blank=True)

    name_eng = models.CharField(max_length=156, blank=True)
    title_eng = models.CharField(max_length=156, blank=True)
    short_descriptions_eng = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class OurMentors(models.Model):
    name = models.CharField(max_length=156, blank=True)
    title = models.CharField(max_length=500, blank=True)
    who_is_the_mentor = models.CharField(max_length=156, blank=True)

    name_ru = models.CharField(max_length=156, blank=True)
    title_ru = models.CharField(max_length=500, blank=True)
    who_is_the_mentor_ru = models.CharField(max_length=156, blank=True)

    name_eng = models.CharField(max_length=156, blank=True)
    title_eng = models.CharField(max_length=500, blank=True)
    who_is_the_mentor_eng = models.CharField(max_length=156, blank=True)

    def __str__(self):
        return self.name


class Mentors(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=156, blank=True)
    name_lasname = models.CharField(max_length=256, blank=True)
    skill = models.CharField(max_length=156, blank=True)

    title_ru = models.CharField(max_length=156, blank=True)
    name_lasname_ru = models.CharField(max_length=256, blank=True)
    skill_ru = models.CharField(max_length=156, blank=True)

    title_eng = models.CharField(max_length=156, blank=True)
    name_lasname_eng = models.CharField(max_length=256, blank=True)
    skill_eng = models.CharField(max_length=156, blank=True)

    def __str__(self):
        return self.title


class Locatsia(models.Model):
    name = models.CharField(max_length=156, blank=True)
    title = models.CharField(max_length=156, blank=True)
    short_titile = models.CharField(max_length=256, blank=True)

    name_ru = models.CharField(max_length=156)
    title_ru = models.CharField(max_length=156, blank=True)
    short_titile_ru = models.CharField(max_length=256, blank=True)

    name_eng = models.CharField(max_length=156, blank=True)
    title_eng = models.CharField(max_length=156)
    short_titile_eng = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class LocatsiaInfo(models.Model):
    title = models.CharField(max_length=156, blank=True)
    image = models.ImageField(blank=True)
    tarif = models.CharField(max_length=256, blank=True)

    title_ru = models.CharField(max_length=156, blank=True)
    tarif_ru = models.CharField(max_length=256, blank=True)

    title_eng = models.CharField(max_length=156, blank=True)
    tarif_eng = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title


class Footer(models.Model):
    motto = models.CharField(max_length=156, blank=True)
    short_descriptions = models.CharField(max_length=256, blank=True)

    motto_ru = models.CharField(max_length=156, blank=True)
    short_descriptions_ru = models.CharField(max_length=256, blank=True)

    motto_eng = models.CharField(max_length=156, blank=True)
    short_descriptions_eng = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.motto
