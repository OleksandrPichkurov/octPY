from django.contrib.auth.models import User
from rest_framework import serializers
from product.models import Product, Media, Characteristic

# TODO creates MediaNested, CharacteristicNested, FeedbackNested

class ProductNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'product_name']

        
class MediaNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        fields = ['id', 'image']


class CharacteristicNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Characteristic
        fields = ['id', 'characteristic']


class ProductSerializer(serializers.ModelSerializer):
    media = MediaNestedSerializer(many=True, read_only=True)
    characteristics = CharacteristicNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_descriptions', 'product_raiting', 'media', 'characteristics']
        

class MediaSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer(read_only = True) 

    class Meta:
        model = Media
        fields = ['id', 'image', 'product']
        

class CharacteristicSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer(read_only = True)

    class Meta:
        model = Characteristic
        fields = ['id', 'characteristic', 'descriptions', 'product']
