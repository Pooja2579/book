from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RecommendationViewSet, search_books, index

# Initialize the router
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'recommendations', RecommendationViewSet)

# Define URL patterns
urlpatterns = [
    path('', index, name='index'),  # Root URL
    path('index/', index, name='index'),  # /index URL
    path('api/search/', search_books, name='search_books'),  # API endpoint for search
]

# Append the router URLs
urlpatterns += router.urls
