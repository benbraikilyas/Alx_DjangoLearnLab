from django.contrib import admin
from .models import Book  # استيراد نموذج الكتاب

# تسجيل النموذج في لوحة التحكم
admin.site.register(Book)
