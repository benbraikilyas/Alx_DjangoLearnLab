from.models import Author, Book
from rest_framework import serializers
from datetime import datetime

# Serializer for Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  

    # تحقق مخصص لضمان عدم تعيين سنة نشر مستقبلية
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future!")
        return value

# Serializer الخاص بـ Author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  
