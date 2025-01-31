from rest_framework import serializers
from students.models import Student

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'place']
