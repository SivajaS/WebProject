from django.shortcuts import render
from .models import Details
from .serializers import DetailsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class Crud(APIView):

    serializer_class = DetailsSerializer#to instert data restapi

    def get(self,request):
        objPerson = Details.objects.all()
        serializer = DetailsSerializer(objPerson, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
    
    def put(self,request,id):
        obj = self.get_object(id)
        serializer = DetailsSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        obj = self.get_object(id)
        obj.delete()
        return Response({'message':'Person deleted'})
