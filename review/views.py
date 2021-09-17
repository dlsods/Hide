from rest_framework.generics import *
from review.serializers import *


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class CreateReviewView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class UpdateReviewView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class DeleteReviewView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer

