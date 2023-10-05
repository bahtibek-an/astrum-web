from django.contrib import admin
from astrumapp.models import *

# Register your models here.
@admin.register(ReportData)
class RepostStudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'nick_name', 'random_code')
    # search_fields = ('full_name', 'nick_name')


