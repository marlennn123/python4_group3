from .models import *
from rest_framework.serializers import ModelSerializer

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ClothesSerializers(ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'