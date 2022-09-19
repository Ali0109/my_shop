from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validata_data):
        print(instance)
        print(validata_data)
        instance.title = validata_data.get("title", instance.title)
        instance.description = validata_data.get("description", instance.description)
        instance.save()
        return instance
