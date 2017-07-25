from rest_framework import serializers, generics
from ..models import Readings, PostData
from django.contrib.auth.models import User


class ReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readings
        # fields = '__all__'
        fields = ('timestamp', 'readings')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class PostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostData
        fields = '__all__'


