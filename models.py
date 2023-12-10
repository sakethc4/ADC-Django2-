from django.db import models

# Create your models here.
class Review(models.Model):
    review_text = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    review_text = models.CharField(max_length=100, blank=True)
