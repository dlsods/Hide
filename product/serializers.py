from rest_framework import serializers

from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = '__all__'

        def create(self, validated_data):
            request = self.context.get('request')
            validated_data['user'] = request.user
            return super().create(validated_data)

