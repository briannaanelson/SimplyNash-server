from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from simplynashapi.models import Category

class CategoryView(ViewSet):
    def retrieve(self, request, pk):
        categories = Category.objects.get(pk = pk)
        serializer = CategorySerializer(categories)
        return Response(serializer.data)

        
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
            


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')