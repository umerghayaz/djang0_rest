from rest_framework import serializers
from .models import *





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['age'] < 12:
            raise serializers.ValidationError({"error": "age should be greater"})
        return data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'