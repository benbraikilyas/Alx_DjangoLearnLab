from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # عرض الأعمدة الرئيسية
    list_filter = ("publication_year", "author")  # إضافة فلاتر للبحث السريع
    search_fields = ("title", "author")  # تفعيل البحث باستخدام العنوان أو المؤلف
