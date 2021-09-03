from django.urls import path
from rest_framework.routers import DefaultRouter

from . import function_based_view
from .views import AuthorView
from .views_v2 import AuthorViewSet

router = DefaultRouter()
router.register(r'author-viewset', AuthorViewSet, basename='author')

urlpatterns = []

# Function base view
urlpatterns += [
    path('authors', function_based_view.get_authors),
    path('update/author', function_based_view.update_authors),
]

# Class based view
urlpatterns += [

]

# ViewSet Based view
urlpatterns += router.urls
