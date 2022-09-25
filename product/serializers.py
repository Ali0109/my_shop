from rest_framework import serializers

from product.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validata_data):
        instance.title = validata_data.get("title", instance.title)
        instance.description = validata_data.get("description", instance.description)
        instance.save()
        return instance


class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = [
            'id',
            'product',
            'file',
        ]

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validata_data):
    #     instance.title = validata_data.get("title", instance.title)
    #     instance.description = validata_data.get("description", instance.description)
    #     instance.save()
    #     return instance