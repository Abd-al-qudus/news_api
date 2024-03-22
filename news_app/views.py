from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorSerializer, NewsSerializer
from .models import Author, News


# Create your views here.
class NewsListApiView(ListCreateAPIView):
    """create news"""
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsDetailsRetrieveView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    lookup_field = 'id'
    queryset = News.objects.all()


class AuthorListApiView(ListCreateAPIView):
    """create news"""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetailsRetrieveView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    lookup_field = 'id'
    queryset = Author.objects.all()