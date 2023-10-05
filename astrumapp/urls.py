from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('uz/kompanita/', kompanita, name="kompanita"),
    path('uz/kursi/', kursi, name="kursi"),
    path('uz/kursini_ichidagi/<int:id>/', kurs_about, name="kurs_about"),
    path('uz/photo/', photo, name="photo"),
    path('uz/karyera/', karyera, name="karyera"),

    path('ru/', index_ru, name="home_ru"),
    path('ru/kompanita/', kompanita_ru, name="kompanita_ru"),
    path('ru/kursi/', kursi_ru, name="kursi_ru"),
    path('ru/kursini_ichidagi/<int:id>/', kurs_about_ru, name="kurs_about_ru"),
    path('ru/photo/', photo_ru, name="photo_ru"),
    path('ru/karyera/', karyera_ru, name="karyera_ru"),

    path('eng/', index_eng, name="home_eng"),
    path('eng/kompanita/', kompanita_eng, name="kompanita_eng"),
    path('eng/kursi/', kursi_eng, name="kursi_eng"),
    path('eng/kursini_ichidagi/<int:id>/', kurs_about_eng, name="kurs_about_eng"),
    path('eng/photo/', photo_eng, name="photo_eng"),
    path('eng/karyera/', karyera_eng, name="karyera_eng"),
    
    path('send-message/', send_message, name="send_message"),
    path('confirm_code/', confirm_code, name="confirm_code")
]
