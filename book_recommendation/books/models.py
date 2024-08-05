from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    rating = models.FloatField()

class Recommendation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Replace with ForeignKey to User model if using Django's auth system
    comment = models.TextField()
    likes = models.PositiveIntegerField(default=0)
