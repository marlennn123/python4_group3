from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'