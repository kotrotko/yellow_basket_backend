from rest_framework import serializers
from backend.flowers.models import Flower

# Serializer for Flower model
class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id', 'sort', 'price', 'color', 'stock']
