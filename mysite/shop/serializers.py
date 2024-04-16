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


class BasketSerializers(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PersonSerializers(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FavoriteSerializers(ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class NewsSerializers(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ColorSerializers(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


