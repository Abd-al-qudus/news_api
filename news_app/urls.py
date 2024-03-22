from django.urls import path
from .views import (
    NewsListApiView, 
    NewsDetailsRetrieveView,
    AuthorListApiView,
    AuthorDetailsRetrieveView
)


urlpatterns = [
    path('api/author/', AuthorListApiView.as_view(), name='authors-list'),
    path('api/author/<int:id>/', AuthorDetailsRetrieveView.as_view(), name='authors-details'),
    path('api/news/', NewsListApiView.as_view(), name='news-list'),
    path('api/news/<int:id>/', NewsDetailsRetrieveView.as_view(), name='news-details'),
]