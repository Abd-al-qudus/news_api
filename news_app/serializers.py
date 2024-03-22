from rest_framework import serializers
from .models import Author, News


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('full_name', 'email',)
        # read_only_fields = ('id',)


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = News
        fields = '__all__'

