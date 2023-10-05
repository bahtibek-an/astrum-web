from django.db import models
from django.utils.text import slugify
from django.utils import timezone

### KURS ICHI abouti
# class Kurs(models.Model):
class ReportData(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=100)
    random_code = models.CharField(max_length=5)
    created_time = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        verbose_name = 'Report Data'
        verbose_name_plural = "Report Data"
        ordering = ('created_time', )

    def __str__(self) -> str:
        return self.phone