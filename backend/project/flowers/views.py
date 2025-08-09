from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Flower
from .serializers import FlowerSerializer

# API View for Flower List
class FlowerListView(APIView):
    def get(self, request):
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View for Flower Detail
class FlowerDetailView(APIView):
    def get(self, request, pk):
        flower = get_object_or_404(Flower, pk=pk)
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


