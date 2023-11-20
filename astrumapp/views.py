from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse

from Akademiya_Haqida.models import *
from Biz_haqimizda.models import *
from Foto_suratlar.models import *
from Kurs_ichi.models import *
from astrumapp.models import *
from Asosiy_Sahifa.models import *
from Cours.models import *
from .models import ReportData

from .forms import *
import requests
import random
from django.core.cache import cache
from uuid import uuid4


def kurs_about(request, id):
    course = get_object_or_404(Courses, id=id)
    news_header = NewsHeader.objects.all()

    trend_dasturi = TreningDasturi.objects.filter(course=id)
    trening_dasturi_answer = TreningDasturiAnswer.objects.filter(course_training__course=id)

    # Fix the next line to use the correct model name: KurslarUchunDarslar
    kurslar_uchun_darslar = KurslarUchunDarslar.objects.all()

    narxlar = Narxlar.objects.all()
    bugungi_tolov = BugungiTolov.objects.all()
    bugungi_tolov_qlayligi = BugungiTolovQulayligi.objects.all()
    oylik_tolov = OylikTolov.objects.all()
    oylik_tolov_qulayligi = OylikTolovQulayligi.objects.all()
    kurs_jadvali = KursJadvali.objects.all()
    kurs_pLan = KursPLan.objects.all()
    # training programs
    training_program = TrainingProgram.objects.filter(course=id)
    course_seasons = []
    if training_program:
        course_seasons = CourseSeason.objects.filter(course_season=training_program[0].id)
    korib_chiqish = KoribChiqish.objects.filter(course=id)

    bitiruvchilar = Bitiruvchilar.objects.all()
    bitiruvchilar_videolar = BitiruvchilarVideolar.objects.all()
    comentarya = Comentarya.objects.all()

    main_course = Courses.objects.all()
    footer = Footer.objects.all()

    mentors = AstrumMentor.objects.filter(course=id)

    return render(request, "kursini_ichidagi.html",
                  {"course": course, "main_course": main_course,
                   "footer": footer, "trend_dasturi": trend_dasturi,
                   "trening_dasturi_answer": trening_dasturi_answer,
                   "kurslar_uchun_darslar": kurslar_uchun_darslar,
                   "narxlar": narxlar, "bugungi_tolov": bugungi_tolov,
                   "bugungi_tolov_qlayligi": bugungi_tolov_qlayligi,
                   "oylik_tolov": oylik_tolov, "oylik_tolov_qulayligi": oylik_tolov_qulayligi,
                   "kurs_jadvali": kurs_jadvali, "kurs_pLan": kurs_pLan,
                   "news_header": news_header, "korib_chiqish": korib_chiqish,
                   "bitiruvchilar": bitiruvchilar, "bitiruvchilar_videolar": bitiruvchilar_videolar,
                   "comentarya": comentarya,
                   # training programs
                   'training_program': training_program,
                   'course_seasons': course_seasons,
                   "mentors": mentors,
                   })


def kurs_about_ru(request, pk):
    courses_ru: object = get_object_or_404(Courses, pk=pk)
    news_header_ru: object = NewsHeader.objects.all()
    prices: object = Narxlar.objects.all()
    trend_dasturi_ru: object = TreningDasturi.objects.all()
    trening_dasturi_answer_ru = TreningDasturiAnswer.objects.all()

    # Fix the next line to use the correct model name: KurslarUchunDarslar
    kurslar_uchun_darslar_ru = KurslarUchunDarslar.objects.all()

    narxlar_ru = Narxlar.objects.all()
    bugungi_tolov_ru = BugungiTolov.objects.all()
    bugungi_tolov_qlayligi_ru = BugungiTolovQulayligi.objects.all()
    oylik_tolov_ru = OylikTolov.objects.all()
    oylik_tolov_qulayligi_ru = OylikTolovQulayligi.objects.all()
    kurs_jadvali_ru = KursJadvali.objects.all()
    kurs_pLan_ru = KursPLan.objects.all()
    # savollar1_ru = Savollar1.objects.all()
    # savollar_javob1_ru = SavollarJavob1.objects.all()
    # savollar2_ru = Savollar2.objects.all()
    # savollar_javob2_ru = SavollarJavob2.objects.all()
    korib_chiqish_ru = KoribChiqish.objects.filter(course=pk)

    bitiruvchilar_ru = Bitiruvchilar.objects.all()
    bitiruvchilar_videolar_ru = BitiruvchilarVideolar.objects.all()
    comentarya_ru = Comentarya.objects.all()

    main_course_ru = Courses.objects.all()
    footer_ru = Footer.objects.all()

    # training programs
    training_program = TrainingProgram.objects.filter(course=pk)
    course_seasons = []
    if training_program:
        course_seasons = CourseSeason.objects.filter(course_season=training_program[0].id)

    mentors = AstrumMentor.objects.filter(course=id)

    ctx = {
        "course_ru": courses_ru, "main_course_ru": main_course_ru,
        "footer_ru": footer_ru, "trend_dasturi_ru": trend_dasturi_ru,
        "trening_dasturi_answer_ru": trening_dasturi_answer_ru,
        "kurslar_uchun_darslar_ru": kurslar_uchun_darslar_ru,
        "narxlar_ru": prices, "bugungi_tolov_ru": bugungi_tolov_ru,
        "bugungi_tolov_qlayligi_ru": bugungi_tolov_qlayligi_ru,
        "oylik_tolov_ru": oylik_tolov_ru, "oylik_tolov_qulayligi_ru": oylik_tolov_qulayligi_ru,
        "kurs_jadvali_ru": kurs_jadvali_ru, "kurs_pLan_ru": kurs_pLan_ru,
        "news_header_ru": news_header_ru, "korib_chiqish_ru": korib_chiqish_ru,
        "bitiruvchilar_ru": bitiruvchilar_ru, "bitiruvchilar_videolar_ru": bitiruvchilar_videolar_ru,
        "comentarya_ru": comentarya_ru,
        # training programs
        'training_program': training_program,
        'course_seasons': course_seasons,
        "mentors": mentors
    }
    return render(request, "kursini_ichidagi-ru.html", ctx)


def kurs_about_eng(request, id):
    course_eng = get_object_or_404(Courses, id=id)
    news_header_eng = NewsHeader.objects.all()

    trend_dasturi_eng = TreningDasturi.objects.all()
    trening_dasturi_answer_eng = TreningDasturiAnswer.objects.all()

    # Fix the next line to use the correct model name: KurslarUchunDarslar
    kurslar_uchun_darslar_eng = KurslarUchunDarslar.objects.all()

    narxlar_eng = Narxlar.objects.all()
    bugungi_tolov_eng = BugungiTolov.objects.all()
    bugungi_tolov_qlayligi_eng = BugungiTolovQulayligi.objects.all()
    oylik_tolov_eng = OylikTolov.objects.all()
    oylik_tolov_qulayligi_eng = OylikTolovQulayligi.objects.all()
    kurs_jadvali_eng = KursJadvali.objects.all()
    kurs_pLan_eng = KursPLan.objects.all()
    try:
        korib_chiqish_eng = KoribChiqish.objects.get(course=id)
    except KoribChiqish.DoesNotExist:
        korib_chiqish_eng = []
    bitiruvchilar_eng = Bitiruvchilar.objects.all()
    bitiruvchilar_videolar_eng = BitiruvchilarVideolar.objects.all()
    comentarya_eng = Comentarya.objects.all()

    main_course_eng = Courses.objects.all()
    footer_eng = Footer.objects.all()

    # training programs
    training_program = TrainingProgram.objects.filter(course=id)
    course_seasons = []
    if training_program:
        course_seasons = CourseSeason.objects.filter(course_season=training_program[0].id)
    mentors = AstrumMentor.objects.filter(course=id)
    return render(request, "kursini_ichidagi-eng.html",
                  {"course_eng": course_eng, "main_course_eng": main_course_eng,
                   "footer_eng": footer_eng, "trend_dasturi_eng": trend_dasturi_eng,
                   "trening_dasturi_answer_eng": trening_dasturi_answer_eng,
                   "kurslar_uchun_darslar_eng": kurslar_uchun_darslar_eng,
                   "narxlar_eng": narxlar_eng, "bugungi_tolov_eng": bugungi_tolov_eng,
                   "bugungi_tolov_qlayligi_eng": bugungi_tolov_qlayligi_eng,
                   "oylik_tolov_eng": oylik_tolov_eng, "oylik_tolov_qulayligi_eng": oylik_tolov_qulayligi_eng,
                   "kurs_jadvali_eng": kurs_jadvali_eng, "kurs_pLan_eng": kurs_pLan_eng,
                   "news_header_eng": news_header_eng, "korib_chiqish_eng": korib_chiqish_eng,
                   "bitiruvchilar_eng": bitiruvchilar_eng, "bitiruvchilar_videolar_eng": bitiruvchilar_videolar_eng,
                   "comentarya_eng": comentarya_eng,
                   # training programs
                   'training_program': training_program,
                   'course_seasons': course_seasons,
                   "mentors": mentors,
                   })


def index(request):
    news_header = NewsHeader.objects.all()
    main_header = MainHeader.objects.all()
    about_us = AboutUs.objects.all()
    why_exactly_sstrum = WhyAstrum.objects.all()
    the_rules = WhyAstrumInfo.objects.all()
    education_courses = CoursInfo.objects.all()
    main_course = Courses.objects.filter(is_main=True)
    why_astrum = WhyAstrumPart2.objects.all()
    why_astrum_answer = WhyAstrumInfo2.objects.all()
    our_mentors = OurMentors.objects.all()
    main_mentors = Mentors.objects.all()
    locatsia = Locatsia.objects.all()
    astrum_locatsia = LocatsiaInfo.objects.all()
    footer = Footer.objects.all()
    theles = Theles.objects.all()

    ctx = {
        "news_header": news_header,
        "main_header": main_header,
        "about_us": about_us,
        "why_exactly_sstrum": why_exactly_sstrum,
        "the_rules": the_rules,
        "education_courses": education_courses,
        "main_course": main_course,
        "why_astrum": why_astrum,
        "why_astrum_answer": why_astrum_answer,
        "our_mentors": our_mentors,
        "main_mentors": main_mentors,
        "locatsia": locatsia,
        "astrum_locatsia": astrum_locatsia,
        "footer": footer,
        "theles": theles,
    }

    return render(request, 'index.html', ctx)


def kompanita(requests):
    news_header = NewsHeader.objects.all()
    main_mentors = Mentors.objects.all()

    akamdeya_haqida = AkademyaHaqidaHeader.objects.all()
    asside_akademya_haqida = AssideAkademiyaHaqida.objects.all()
    asside_talim_tizimi = AssideTalimTizimi.objects.all()
    asside_qulaylik = AssideQulaylik.objects.all()
    asside_kurslar = AssideKurslar.objects.all()
    asside_oqituvchilar = AssideOqituvchilar.objects.all()
    asside_mashgulotlar_kurslar = AssideMashgulotKurslari.objects.all()

    main_course = Courses.objects.all()
    footer = Footer.objects.all()

    ctx = {
        "news_header": news_header,
        "main_mentors": main_mentors,

        "akamdeya_haqida": akamdeya_haqida,
        "asside_akademya_haqida": asside_akademya_haqida,
        "asside_talim_tizimi": asside_talim_tizimi,
        "asside_qulaylik": asside_qulaylik,
        "asside_kurslar": asside_kurslar,
        "asside_oqituvchilar": asside_oqituvchilar,
        "asside_mashgulotlar_kurslar": asside_mashgulotlar_kurslar,

        "main_course": main_course,
        "footer": footer,
    }
    return render(requests, 'kompanita.html', ctx)


def kursi(requests):
    news_header = NewsHeader.objects.all()
    kursi = Kurslar.objects.all()

    main_course = Courses.objects.all()
    footer = Footer.objects.all()

    ctx = {
        "news_header": news_header,
        "kursi": kursi,

        "main_course": main_course,
        "footer": footer,
    }
    return render(requests, 'kursi.html', ctx)


def photo(requests):
    news_header = NewsHeader.objects.all()
    photo = Photo.objects.all()
    complex = KompleksJoylashmalar.objects.all()
    ourcourses = BizningKurslarimiz.objects.all()
    complexlive = KompanyaIchidagiHayot.objects.all()

    main_course = Courses.objects.all()
    footer = Footer.objects.all()

    ctx = {
        "complexlive": complexlive,
        "ourcourses": ourcourses,
        "complex": complex,
        "news_header": news_header,
        "photo": photo,

        "main_course": main_course,
        "footer": footer,

    }
    return render(requests, 'photo.html', ctx)


def karyera(requests):
    news_header = NewsHeader.objects.all()
    karyera = Karyera.objects.all()
    vakansiya = Vakansiya.objects.all()

    main_course = Courses.objects.all()
    footer = Footer.objects.all()

    ctx = {

        "news_header": news_header,
        "karyera": karyera,
        "vakansiya": vakansiya,

        "main_course": main_course,
        "footer": footer,
    }
    return render(requests, 'karyera.html', ctx)


def index_ru(request):
    news_header_ru = NewsHeader.objects.all()
    main_header_ru = MainHeader.objects.all()
    about_us_ru = AboutUs.objects.all()
    why_exactly_sstrum_ru = WhyAstrum.objects.all()
    the_rules_ru = WhyAstrumInfo.objects.all()
    education_courses_ru = CoursInfo.objects.all()
    main_course_ru = Courses.objects.all()
    why_astrum_ru = WhyAstrumPart2.objects.all()
    why_astrum_answer_ru = WhyAstrumInfo2.objects.all()
    our_mentors_ru = OurMentors.objects.all()
    main_mentors_ru = Mentors.objects.all()
    locatsia_ru = Locatsia.objects.all()
    astrum_locatsia_ru = LocatsiaInfo.objects.all()
    footer_ru = Footer.objects.all()
    theles = Theles.objects.all()

    ctx = {
        "news_header_ru": news_header_ru,
        "main_header_ru": main_header_ru,
        "about_us_ru": about_us_ru,
        "why_exactly_sstrum_ru": why_exactly_sstrum_ru,
        "the_rules_ru": the_rules_ru,
        "education_courses_ru": education_courses_ru,
        "main_course_ru": main_course_ru,
        "why_astrum_ru": why_astrum_ru,
        "why_astrum_answer_ru": why_astrum_answer_ru,
        "our_mentors_ru": our_mentors_ru,
        "main_mentors_ru": main_mentors_ru,
        "locatsia_ru": locatsia_ru,
        "astrum_locatsia_ru": astrum_locatsia_ru,
        "footer_ru": footer_ru,
        "theles": theles,
    }

    return render(request, 'index-ru.html', ctx)


def index_eng(request):
    news_header_eng = NewsHeader.objects.all()
    main_header_eng = MainHeader.objects.all()
    about_us_eng = AboutUs.objects.all()
    why_exactly_sstrum_eng = WhyAstrum.objects.all()
    the_rules_eng = WhyAstrumInfo.objects.all()
    education_courses_eng = CoursInfo.objects.all()
    main_course_eng = Courses.objects.all()
    why_astrum_eng = WhyAstrumPart2.objects.all()
    why_astrum_answer_eng = WhyAstrumInfo2.objects.all()
    our_mentors_eng = OurMentors.objects.all()
    main_mentors_eng = Mentors.objects.all()
    locatsia_eng = Locatsia.objects.all()
    astrum_locatsia_eng = LocatsiaInfo.objects.all()
    footer_eng = Footer.objects.all()

    ctx = {
        "news_header_eng": news_header_eng,
        "main_header_eng": main_header_eng,
        "about_us_eng": about_us_eng,
        "why_exactly_sstrum_eng": why_exactly_sstrum_eng,
        "the_rules_eng": the_rules_eng,
        "education_courses_eng_eng": education_courses_eng,
        "main_course_eng": main_course_eng,
        "why_astrum_eng": why_astrum_eng,
        "why_astrum_answer_eng": why_astrum_answer_eng,
        "our_mentors_eng": our_mentors_eng,
        "main_mentors_eng": main_mentors_eng,
        "locatsia_eng": locatsia_eng,
        "astrum_locatsia_eng": astrum_locatsia_eng,
        "footer_eng": footer_eng,
    }

    return render(request, 'index-eng.html', ctx)


def kompanita_ru(requests):
    news_header_ru = NewsHeader.objects.all()
    main_mentors_ru = Mentors.objects.all()

    akamdeya_haqida_ru = AkademyaHaqidaHeader.objects.all()
    asside_akademya_haqida_ru = AssideAkademiyaHaqida.objects.all()
    asside_talim_tizimi_ru = AssideTalimTizimi.objects.all()
    asside_qulaylik_ru = AssideQulaylik.objects.all()
    asside_kurslar_ru = AssideKurslar.objects.all()
    asside_oqituvchilar_ru = AssideOqituvchilar.objects.all()
    asside_mashgulotlar_kurslar_ru = AssideMashgulotKurslari.objects.all()

    main_course_ru = Courses.objects.all()
    footer_ru = Footer.objects.all()

    ctx = {
        "news_header_ru": news_header_ru,
        "main_mentors_ru": main_mentors_ru,

        "akamdeya_haqida_ru": akamdeya_haqida_ru,
        "asside_akademya_haqida_ru": asside_akademya_haqida_ru,
        "asside_talim_tizimi_ru": asside_talim_tizimi_ru,
        "asside_qulaylik_ru": asside_qulaylik_ru,
        "asside_kurslar_ru": asside_kurslar_ru,
        "asside_oqituvchilar_ru": asside_oqituvchilar_ru,
        "asside_mashgulotlar_kurslar_ru": asside_mashgulotlar_kurslar_ru,

        "main_course_ru": main_course_ru,
        "footer_ru": footer_ru,
    }
    return render(requests, 'kompanita-ru.html', ctx)


def kompanita_eng(requests):
    news_header_eng = NewsHeader.objects.all()
    main_mentors_eng = Mentors.objects.all()

    akamdeya_haqida_eng = AkademyaHaqidaHeader.objects.all()
    asside_akademya_haqida_eng = AssideAkademiyaHaqida.objects.all()
    asside_talim_tizimi_eng = AssideTalimTizimi.objects.all()
    asside_qulaylik_eng = AssideQulaylik.objects.all()
    asside_kurslar_eng = AssideKurslar.objects.all()
    asside_oqituvchilar_eng = AssideOqituvchilar.objects.all()
    asside_mashgulotlar_kurslar_eng = AssideMashgulotKurslari.objects.all()

    main_course_eng = Courses.objects.all()
    footer_eng = Footer.objects.all()

    ctx = {
        "news_header_eng": news_header_eng,
        "main_mentors_eng": main_mentors_eng,

        "akamdeya_haqida_eng": akamdeya_haqida_eng,
        "asside_akademya_haqida_eng": asside_akademya_haqida_eng,
        "asside_talim_tizimi_eng": asside_talim_tizimi_eng,
        "asside_qulaylik_eng": asside_qulaylik_eng,
        "asside_kurslar_eng": asside_kurslar_eng,
        "asside_oqituvchilar_eng": asside_oqituvchilar_eng,
        "asside_mashgulotlar_kurslar_eng": asside_mashgulotlar_kurslar_eng,

        "main_course_eng": main_course_eng,
        "footer_eng": footer_eng,
    }
    return render(requests, 'kompanita-eng.html', ctx)


def kursi_ru(requests):
    news_header_ru = NewsHeader.objects.all()
    kursi_ru = Kurslar.objects.all()

    main_course_ru = Courses.objects.all()
    footer_ru = Footer.objects.all()

    ctx = {
        "news_header_ru": news_header_ru,
        "kursi_ru": kursi_ru,

        "main_course_ru": main_course_ru,
        "footer_ru": footer_ru,
    }
    return render(requests, 'kursi-ru.html', ctx)


def kursi_eng(requests):
    news_header_eng = NewsHeader.objects.all()
    kursi_eng = Kurslar.objects.all()

    main_course_eng = Courses.objects.all()
    footer_eng = Footer.objects.all()

    ctx = {
        "news_header_eng": news_header_eng,
        "kursi_eng": kursi_eng,

        "main_course_eng": main_course_eng,
        "footer_eng": footer_eng,
    }
    return render(requests, 'kursi-eng.html', ctx)


def photo_ru(requests):
    complex_ru = KompleksJoylashmalar.objects.all()
    ourcourses_ru = BizningKurslarimiz.objects.all()
    complexlive_ru = KompanyaIchidagiHayot.objects.all()
    news_header_ru = NewsHeader.objects.all()
    photo_ru = Photo.objects.all()

    main_course_ru = Courses.objects.all()
    footer_ru = Footer.objects.all()

    ctx = {
        "complexlive_ru": complexlive_ru,
        "ourcourses_ru": ourcourses_ru,
        "complex_ru": complex_ru,
        "news_header_ru": news_header_ru,
        "photo_ru": photo_ru,

        "main_course_ru": main_course_ru,
        "footer_ru": footer_ru,

    }
    return render(requests, 'photo-ru.html', ctx)


def photo_eng(requests):
    complex_eng = KompleksJoylashmalar.objects.all()
    ourcourses_eng = BizningKurslarimiz.objects.all()
    complexlive_eng = KompanyaIchidagiHayot.objects.all()
    news_header_eng = NewsHeader.objects.all()
    photo_eng = Photo.objects.all()

    main_course_eng = Courses.objects.all()
    footer_eng = Footer.objects.all()

    ctx = {
        "complexlive_eng": complexlive_eng,
        "ourcourses_eng": ourcourses_eng,
        "complex_eng": complex_eng,
        "news_header_eng": news_header_eng,
        "photo_eng": photo_eng,

        "main_course_eng": main_course_eng,
        "footer_eng": footer_eng,

    }
    return render(requests, 'photo-eng.html', ctx)


def karyera_ru(requests):
    news_header_ru = NewsHeader.objects.all()
    karyera_ru = Karyera.objects.all()
    vakansiya_ru = Vakansiya.objects.all()

    main_course_ru = Courses.objects.all()
    footer_ru = Footer.objects.all()

    ctx = {

        "news_header_ru": news_header_ru,
        "karyera_ru": karyera_ru,
        "vakansiya_ru": vakansiya_ru,

        "main_course_ru": main_course_ru,
        "footer_ru": footer_ru,
    }
    return render(requests, 'karyera-ru.html', ctx)


def karyera_eng(requests):
    news_header_eng = NewsHeader.objects.all()
    karyera_eng = Karyera.objects.all()
    vakansiya_eng = Vakansiya.objects.all()

    main_course_eng = Courses.objects.all()
    footer_eng = Footer.objects.all()

    ctx = {
        "news_header_eng": news_header_eng,
        "karyera_eng": karyera_eng,
        "vakansiya_eng": vakansiya_eng,

        "main_course_eng": main_course_eng,
        "footer_eng": footer_eng,
    }
    return render(requests, 'karyera-eng.html', ctx)


def send_message(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            full_name = form.cleaned_data["full_name"]
            nick_name = form.cleaned_data["nick_name"]
            unique_id = uuid4()
            random_code = random.randint(1000, 9999)
            data = {
                "header": {
                    "login": "sms0069ts",
                    "pwd": "1234qaz",
                    "CgPN": 1490
                },
                "body": {
                    "message_id_in": str(unique_id),
                    "CdPN": phone,
                    "text": "Your code: " + str(random_code)
                }
            }
            response = requests.post('http://sms.etc.uz:8084/single-sms', json=data)
            if response.status_code == 200:
                data = ReportData.objects.create(phone=phone, random_code=random_code, full_name=full_name,
                                                 nick_name=nick_name)
                data.save()
                status_data = {'status': 'success'}
                response = JsonResponse(status_data, status=200)
                return response
            status_data = {'status': 'error'}
            response = JsonResponse(status_data, status=400)
            return response

    return render(request, "index.html", {"form": form})


def confirm_code(request):
    if request.method == "POST":
        form = ConfirmForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            code = form.cleaned_data["code"]
            full_name = form.cleaned_data["full_name"]
            nick_name = form.cleaned_data["nick_name"]

            try:
                data_report = ReportData.objects.filter(phone=phone).order_by('-created_time').first()

                if data_report.random_code == code:
                    status_data = {'status': 'success'}

                    data = {
                        "fields": {
                            "TITLE": "Astrum website",
                            "NAME": full_name.split(' ')[0].title(),
                            "LAST_NAME": full_name.split(' ')[1].title(),
                            "STATUS_ID": "NEW",
                            "OPENED": "Y",
                            "SOURCE_ID": "UC_TIAVP5",
                            "ASSIGNED_BY_ID": 1,
                            "PHONE": [
                                {
                                    "VALUE": str(phone),
                                    "VALUE_TYPE": "WORK"
                                }
                            ],
                            # "EMAIL": [
                            #     {
                            #         "VALUE": nick_name,
                            #         "VALUE_TYPE": "WORK"
                            #     }
                            # ]
                        },
                        "params": {
                            "REGISTER_SONET_EVENT": "Y"
                        }
                    }

                    print(data)

                    responseBitrix = requests.post(
                        'https://office.astrum.uz/rest/33/eko4d7ti6fax0tx1/crm.lead.add.json', json=data)

                    response = JsonResponse(status_data, status=200)
                    return response
                return JsonResponse({'status': 'code invalid'}, status=400)
            except:
                return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'status': 'get method'}, status=400)

### English tili qismiii ###
