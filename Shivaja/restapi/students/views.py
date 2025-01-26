from django.shortcuts import render
from students.serializer import StudentsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from students.models import Student
from rest_framework import status

@api_view(['GET', 'POST','DELETE'])
def studentlist(request):
    if request.method == 'GET':
        students = Student.objects.all()
        s = StudentsSerializer(students, many=True)
        return Response(s.data)
    elif request.method == 'POST':
        if not request.data:
            return Response({"error": "Request data is empty"}, status=status.HTTP_400_BAD_REQUEST)
        s = StudentsSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def studentsdetails(request, pk):
    try:
        s_detail = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        s = StudentsSerializer(s_detail)
        return Response(s.data)
    elif request.method == 'PUT':
        s = StudentsSerializer(s_detail, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        s_detail.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
