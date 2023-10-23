from django.core.validators import FileExtensionValidator
from django.db import models
from Cours.models import Courses


class TreningDasturi(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=250)

    title_ru = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=250)

    title_eng = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class KoribChiqish(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    descriptions = models.TextField(blank=True, null=True)

    title_ru = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=250)
    descriptions_ru = models.TextField(blank=True, null=True)

    title_eng = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=250)
    descriptions_eng = models.TextField(blank=True, null=True)

    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.title


class Bitiruvchilar(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=500)

    title_ru = models.CharField(max_length=100)
    descriptions_ru = models.CharField(max_length=500)

    title_eng = models.CharField(max_length=100)
    descriptions_eng = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class BitiruvchilarVideolar(models.Model):
    name_lastname = models.CharField(max_length=256)
    skill = models.CharField(max_length=500)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    name_lastname_ru = models.CharField(max_length=256)
    skill_ru = models.CharField(max_length=500)

    name_lastname_eng = models.CharField(max_length=256)
    skill_eng = models.CharField(max_length=500)

    def __str__(self):
        return self.name_lastname


class Comentarya(models.Model):
    name_lastname = models.CharField(max_length=156)
    skill = models.CharField(max_length=256)
    descriptions = models.CharField(max_length=500)
    image = models.ImageField(blank=True)

    name_lastname_ru = models.CharField(max_length=156)
    skill_ru = models.CharField(max_length=256)
    descriptions_ru = models.CharField(max_length=500)

    name_lastname_eng = models.CharField(max_length=156)
    skill_eng = models.CharField(max_length=256)
    descriptions_eng = models.CharField(max_length=500)

    def __str__(self):
        return self.name_lastname


class TreningDasturiAnswer(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=250)

    title_ru = models.CharField(max_length=100)
    descriptions_ru = models.CharField(max_length=250)

    title_eng = models.CharField(max_length=100)
    descriptions_eng = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class KurslarUchunDarslar(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to="kurs_ichi/")
    image2 = models.ImageField(upload_to="kurs_ichi/")
    image3 = models.ImageField(upload_to="kurs_ichi/")
    image4 = models.ImageField(upload_to="kurs_ichi/")
    image5 = models.ImageField(upload_to="kurs_ichi/")

    name_ru = models.CharField(max_length=100)
    descriptions_ru = models.CharField(max_length=250)

    name_eng = models.CharField(max_length=100)
    descriptions_eng = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Narxlar(models.Model):
    name = models.CharField(max_length=250)
    descriptions = models.CharField(max_length=500)

    name_ru = models.CharField(max_length=250)
    descriptions_ru = models.CharField(max_length=500)

    name_eng = models.CharField(max_length=250)
    descriptions_eng = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class BugungiTolov(models.Model):
    oylik_tolov_chegirma = models.CharField(max_length=100)
    skidka = models.CharField(max_length=100)
    narx_oyiga = models.CharField(max_length=100)
    kurs_name = models.CharField(max_length=100)
    kurs_narx = models.CharField(max_length=100)
    skidka_text = models.CharField(max_length=100)
    skidka_narx = models.CharField(max_length=100)
    jami_skidka = models.CharField(max_length=100)
    jami_narx = models.CharField(max_length=100)

    oylik_tolov_chegirma_ru = models.CharField(max_length=100)
    skidka_ru = models.CharField(max_length=100)
    narx_oyiga_ru = models.CharField(max_length=100)
    kurs_name_ru = models.CharField(max_length=100)
    kurs_narx_ru = models.CharField(max_length=100)
    skidka_text_ru = models.CharField(max_length=100)
    skidka_narx_ru = models.CharField(max_length=100)
    jami_skidka_ru = models.CharField(max_length=100)
    jami_narx_ru = models.CharField(max_length=100)

    oylik_tolov_chegirma_eng = models.CharField(max_length=100)
    skidka_eng = models.CharField(max_length=100)
    narx_oyiga_eng = models.CharField(max_length=100)
    kurs_name_eng = models.CharField(max_length=100)
    kurs_narx_eng = models.CharField(max_length=100)
    skidka_text_eng = models.CharField(max_length=100)
    skidka_narx_eng = models.CharField(max_length=100)
    jami_skidka_eng = models.CharField(max_length=100)
    jami_narx_eng = models.CharField(max_length=100)

    def __str__(self):
        return self.oylik_tolov_chegirma


class BugungiTolovQulayligi(models.Model):
    title = models.CharField(max_length=500)

    title_ru = models.CharField(max_length=500)

    title_eng = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class OylikTolov(models.Model):
    oyiga = models.CharField(max_length=100)
    besh_x_oylik_tolovlar = models.CharField(max_length=100)
    jami_narx = models.CharField(max_length=100)

    oyiga_ru = models.CharField(max_length=100)
    besh_x_oylik_tolovlar_ru = models.CharField(max_length=100)
    jami_narx_ru = models.CharField(max_length=100)

    oyiga_eng = models.CharField(max_length=100)
    besh_x_oylik_tolovlar_eng = models.CharField(max_length=100)
    jami_narx_eng = models.CharField(max_length=100)

    def __str__(self):
        return self.oyiga


class OylikTolovQulayligi(models.Model):
    title = models.CharField(max_length=500)

    title_ru = models.CharField(max_length=500)

    title_eng = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class KursJadvali(models.Model):
    name = models.CharField(max_length=156)
    descriptions = models.CharField(max_length=156)

    name_ru = models.CharField(max_length=156)
    descriptions_ru = models.CharField(max_length=156)

    name_eng = models.CharField(max_length=156)
    descriptions_eng = models.CharField(max_length=156)

    def __str__(self):
        return self.name


class KursPLan(models.Model):
    kurs_name = models.CharField(max_length=156)
    data = models.CharField(max_length=500)
    oqish_davomiligi = models.CharField(max_length=156)
    name_lastname = models.CharField(max_length=156)
    image = models.ImageField(upload_to="kurs_ichi/")
    sohasi = models.CharField(max_length=156)

    kurs_name_ru = models.CharField(max_length=156)
    data_ru = models.CharField(max_length=500)
    oqish_davomiligi_ru = models.CharField(max_length=156)
    name_lastname_ru = models.CharField(max_length=156)
    sohasi_ru = models.CharField(max_length=156)

    kurs_name_eng = models.CharField(max_length=156)
    data_eng = models.CharField(max_length=500)
    oqish_davomiligi_eng = models.CharField(max_length=156)
    name_lastname_eng = models.CharField(max_length=156)
    sohasi_eng = models.CharField(max_length=156)

    def __str__(self):
        return self.kurs_name


class TrainingProgram(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True,
                               related_name="training_programs")

    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    course_structure = models.TextField()

    title_ru = models.CharField(max_length=200)
    descriptions_ru = models.TextField()
    course_structure_ru = models.TextField()

    title_en = models.CharField(max_length=200)
    descriptions_en = models.TextField()
    course_structure_en = models.TextField()

    class Meta:
        verbose_name = "Учебная программа"
        verbose_name_plural = "Учебные программы"

    def __str__(self):
        return self.title_ru


class CourseSeason(models.Model):
    course_season = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name="course_seasons")

    title = models.CharField(max_length=200)
    description = models.TextField()

    title_ru = models.CharField(max_length=200)
    description_ru = models.TextField()

    title_en = models.CharField(max_length=200)
    description_en = models.TextField()

    class Meta:
        verbose_name = "Сезон курса"
        verbose_name_plural = "Сезоны курса"

    def __str__(self):
        return self.title_ru


class QuestionAndAnswers(models.Model):
    course_season = models.ForeignKey(CourseSeason, on_delete=models.CASCADE, related_name="question_and_answers")
    question = models.CharField(max_length=400)
    answer = models.TextField()

    question_ru = models.CharField(max_length=400, default="test")
    answer_ru = models.TextField()

    question_en = models.CharField(max_length=400)
    answer_en = models.TextField()

    class Meta:
        verbose_name_plural = "Вопросы и ответы"
        verbose_name = "Вопрос и ответ"

    def __str__(self):
        return self.question_ru
