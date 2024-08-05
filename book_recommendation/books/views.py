from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Recommendation
from .serializers import BookSerializer, RecommendationSerializer
from .utils import fetch_books_from_google

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

@api_view(['GET'])
def search_books(request):
    query = request.GET.get('q', '')  # Ensure 'q' is the query parameter
    if not query:
        return Response({"error": "Query parameter 'q' is required."}, status=400)

    # Fetch books from Google Books API
    data = fetch_books_from_google(query)
    if data:
        return Response(data)
    return Response({"error": "Unable to fetch data from Google Books API."}, status=500)

def index(request):
    return render(request, 'index.html')
