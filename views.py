from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.objects.filter():
            review_data = {
                'name' : review.name,
                'email' : review.email,
                'phone_number' : review.phone_number,
                'review_text' : review.review_text,
            }
            reviews.append(review.review_text)
        return Response({'reviews': reviews})

class CreateAppDevClubReview(APIView):
    def post(self, request):
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        phone_number = request.data.get('phone_number', '')
        review_text = request.data.get('review_text', '')

        if review_text != '':
            new_database_entry = Review(
                name=name,
                email=email,
                phone_number=phone_number,
                review_text=review_text
            )
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})