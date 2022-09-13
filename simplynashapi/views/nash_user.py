from dataclasses import fields
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplynashapi.models import NashUser

class NashUserView(ViewSet):
    def retrieve(self, request, pk):
        nashuser = NashUser.objects.get(pk=pk)
        serializer = NashUserSerializer(nashuser)
        return Response(serializer.data)
    
    def list(self, request):
        nashuser = NashUser.objects.all()
        serializer = NashUserSerializer(nashuser, many=True)
        return Response(serializer.data)
        

class NashUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NashUser
        fields = ('id','user')