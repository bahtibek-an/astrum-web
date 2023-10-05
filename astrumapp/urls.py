from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('uz/about_academy/', kompanita, name="kompanita"),
    path('uz/courses/', kursi, name="kursi"),
    path('uz/courses/<int:id>/', kurs_about, name="kurs_about"),
    path('uz/photo/', photo, name="photo"),
    path('uz/about_us/', karyera, name="karyera"),

    path('ru/', index_ru, name="home_ru"),
    path('ru/about_academy/', kompanita_ru, name="kompanita_ru"),
    path('ru/courses/', kursi_ru, name="kursi_ru"),
    path('ru/courses/<int:id>/', kurs_about_ru, name="kurs_about_ru"),
    path('ru/photo/', photo_ru, name="photo_ru"),
    path('ru/about_us/', karyera_ru, name="karyera_ru"),

    path('eng/', index_eng, name="home_eng"),
    path('eng/about_academy/', kompanita_eng, name="kompanita_eng"),
    path('eng/courses/', kursi_eng, name="kursi_eng"),
    path('eng/courses/<int:id>/', kurs_about_eng, name="kurs_about_eng"),
    path('eng/photo/', photo_eng, name="photo_eng"),
    path('eng/about_us/', karyera_eng, name="karyera_eng"),
    
    path('send-message/', send_message, name="send_message"),
    path('confirm_code/', confirm_code, name="confirm_code")
]
