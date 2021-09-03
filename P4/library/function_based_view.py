from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthorSerializer
from django.http.response import JsonResponse
from .models import Author


@api_view(http_method_names=['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(
        {'authors': serializer.data}
    )


@api_view(http_method_names=['POST'])
def update_authors(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
