from rest_framework import serializers
from .models import Author

choices = ('male', 'female')


class AuthorSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=choices)

    class Meta:
        model = Author
        fields = '__all__'


class AuthorNameSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=choices, read_only=True)
    dead = serializers.BooleanField(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
