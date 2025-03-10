from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    published_date = models.DateField(null=True, blank=True)  # تاريخ النشر (اختياري)

    def __str__(self):
        return self.title       
    