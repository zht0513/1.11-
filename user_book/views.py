from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import status
# Create your views here.
from rest_framework.response import Response

from user_book.models import Book
from user_book.response import APIResponse
from user_book.serialiezr import BookModelSerializer


class BookGenericsAPIView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    lookup_field = 'id'

    # def get(self, request, *args, **kwargs):
    #     if 'id' in kwargs:
    #         return self.retrieve(request, *args, **kwargs)
    #     else:
    #         return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     response = self.create(request, *args, **kwargs)
    #     return Response({
    #         "message": "成功",
    #         "results": BookModelSerializer(response).data,
    #     }, status=status.HTTP_200_OK)
    #
    # def put(self, request, *args, **kwargs):
    #     response = self.update(request, *args, **kwargs)
    #     return Response({
    #         "message": "成功",
    #         "results": BookModelSerializer(response).data,
    #     }, status=status.HTTP_200_OK)
    #
    # def patch(self, request, *args, **kwargs):
    #     response = self.partial_update(request, *args, **kwargs)
    #     return Response({
    #         "message": "成功",
    #         "results": BookModelSerializer(response).data,
    #     }, status=status.HTTP_200_OK)
    #
    # def delete(self, request, *args, **kwargs):
    #     response = self.destroy(request, *args, **kwargs)
    #     return Response({
    #         "message": "成功",
    #         "results": BookModelSerializer(response).data,
    #     }, status=status.HTTP_200_OK)
    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(results=response.data)