from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from library.models import Author
from django.shortcuts import get_object_or_404
from library.serializers import AuthorSerializer, AuthorNameSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


# class AuthorViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Author.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = AuthorSerializer(user)
#         return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    http_method_names = ['get', 'post', 'put']

    def get_serializer_class(self):
        if self.action == 'change_name':
            return AuthorNameSerializer
        else:
            return AuthorSerializer

    @action(detail=True, methods=['get', 'post'])
    def change_name(self, request, pk=None):
        if request.method == 'GET':
            author = get_object_or_404(self.queryset, pk=pk)
            serializer = AuthorNameSerializer(author)
            return Response(serializer.data)
        elif request.method == 'POST':
            author = get_object_or_404(self.queryset, pk=pk)
            serializer = AuthorNameSerializer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'name changed'})
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
