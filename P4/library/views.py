from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer
from django.shortcuts import get_object_or_404

from .models import Author


class AuthorView(APIView):

    def get(self, request):
        authos = Author.objects.all()
        return Response({"authors": authos})

    # def get(self, request):
    #     authors = Author.objects.all()
    #     # the many param informs the serializer that it will be serializing more than a single article.
    #     serializer = AuthorSerializer(authors, many=True)
    #     return Response({"authors": serializer.data})

    def post(self, request):
        data = request.data.get('author')

        # Create an article from the above data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Author '{}' created successfully".format(article_saved.name)})

    def put(self, request, pk):
        saved_author = get_object_or_404(Author.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = AuthorSerializer(instance=saved_author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Author '{}' updated successfully".format(article_saved.title)})

    def delete(self, request, pk):
        # Get object with this pk
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response({"message": "Author with id `{}` has been deleted.".format(pk)}, status=204)
