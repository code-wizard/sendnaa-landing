from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from landing import serializers
# Create your views here.


class SAJoinListAPIView(CreateAPIView):
    serializer_class = serializers.SAJoinListSerializer

