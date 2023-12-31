from Kurs_ichi.models import *
from django.contrib import admin
from .models import TrainingProgram, QuestionAndAnswers, CourseSeason
from tinymce.widgets import TinyMCE


# Определяем административный класс для модели QuestionAndAnswers
class QuestionAndAnswersInline(admin.TabularInline):
    model = QuestionAndAnswers
    extra = 1  # Количество пустых форм для добавления вопросов и ответов


class CourseSeasonInline(admin.TabularInline):
    model = CourseSeason
    extra = 1


class CourseSeasonAdmin(admin.ModelAdmin):
    list_display = ('course_season', 'title_ru', 'title_ru')
    list_filter = ('course_season',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    inlines = [QuestionAndAnswersInline]


# Определяем административный класс для модели TrainingProgram
class TrainingProgramAdmin(admin.ModelAdmin):
    # Определяем отображаемые поля в списке объектов
    list_display = ('title_ru', 'course')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    inlines = [CourseSeasonInline]

    # Добавляем фильтры для удобства поиска и фильтрации
    list_filter = ('course',)

    # Поля, по которым можно искать объекты
    search_fields = ('title_ru', 'course__name')


class KoribChiqishAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'course')
    list_filter = ('course',)


class TreningDasturiAnswerInline(admin.TabularInline):
    model = TreningDasturiAnswer
    extra = 1


class TreningDasturiAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'course')
    list_filter = ('course',)
    inlines = [TreningDasturiAnswerInline]


class TreningDasturiAnswerAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'course_training')
    list_filter = ('course_training',)


class MentorAdmin(admin.ModelAdmin):
    list_display = ('full_name_ru', 'course', 'job_title_ru')


admin.site.register(AstrumMentor, MentorAdmin)

admin.site.register(KoribChiqish, KoribChiqishAdmin)

# Регистрируем административный класс TrainingProgram с вложенным QuestionAndAnswersInline
admin.site.register(TrainingProgram, TrainingProgramAdmin)

# Регистрируем административный класс для модели QuestionAndAnswers (можно опционально)
admin.site.register(QuestionAndAnswers)
admin.site.register(CourseSeason, CourseSeasonAdmin)

admin.site.register(TreningDasturi, TreningDasturiAdmin)
admin.site.register(TreningDasturiAnswer, TreningDasturiAnswerAdmin)
admin.site.register(KurslarUchunDarslar)
admin.site.register(Narxlar)
admin.site.register(BugungiTolov)
admin.site.register(BugungiTolovQulayligi)
admin.site.register(OylikTolov)
admin.site.register(OylikTolovQulayligi)

admin.site.register(Bitiruvchilar)
admin.site.register(BitiruvchilarVideolar)
admin.site.register(Comentarya)

admin.site.register(KursJadvali)
admin.site.register(KursPLan)
