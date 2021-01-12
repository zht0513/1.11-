from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from user_book.models import Book, Press


# 出版社
class HouseModelSerializer(ModelSerializer):
    class Meta:
        model = Press
        fields = ('id', 'press_name', 'address')


class BookModelSerializer(ModelSerializer):
    publish = HouseModelSerializer()

    class Meta:
        model = Book
        fields = ["book_name", "price", "publish", "authors", "pic"]
        extra_kwargs = {
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
            "pic": {
                "read_only": True
            },
        }
