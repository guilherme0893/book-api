from rest_framework import serializers
from api.models import AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    # books = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='books'
    # )
    class Meta:
        model = AuthorModel
        fields = '__all__'
