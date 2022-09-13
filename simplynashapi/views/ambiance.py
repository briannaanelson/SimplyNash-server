from dataclasses import fields
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework import serializers, status
from simplynashapi.models import Ambiance



class AmbianceTypeView(ViewSet):
    def retrieve(self, request, pk):
        
        try:
            ambiance = Ambiance.objects.get(pk=pk)
            serializer = AmbianceTypeSerializer(ambiance)
            return Response(serializer.data)
        except Ambiance.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        ambiances = Ambiance.objects.all()
        serializer = AmbianceTypeSerializer(ambiances, many=True)
        return Response(serializer.data)


class AmbianceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiance
        fields = ('id', 'label')