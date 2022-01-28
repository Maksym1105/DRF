from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    # cat_id = serializers.SlugRelatedField(slug_field='cat_id', read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'cat_id', 'use', 'diametr', 'len', 'color', 'photo')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
