from rest_framework import serializers
from .models import book

class BookSerializer(serializers.ModelSerializer):  # ✅ استخدم ModelSerializer بحروف كبيرة
    class Meta:
        model = book
        fields = '__all__'  # ✅ استخدم '__all__' لتضمين جميع الحقول