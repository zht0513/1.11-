from django.urls import path

from user_book import views

urlpatterns = [
    path("book/", views.BookGenericsAPIView.as_view()),
    path("book/<str:id>/", views.BookGenericsAPIView.as_view()),
]