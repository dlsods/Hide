from rest_framework import serializers

from review.models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = '__all__'

        def create(self, validated_data):
            request = self.context.get('request')
            validated_data['user'] = request.user
            return super().create(validated_data)

