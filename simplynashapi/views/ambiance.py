from dataclasses import fields
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework import serializers, status
from simplynashapi.models import Ambiance



class AmbianceTypeView(ViewSet):
   
    def list(self, request):
        ambiances = Ambiance.objects.all()
        serializer = AmbianceTypeSerializer(ambiances, many=True)
        return Response(serializer.data)


class AmbianceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiance
        fields = ('id', 'label')