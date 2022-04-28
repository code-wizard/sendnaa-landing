from rest_framework import serializers
from landing import models


class SAJoinListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = models.SAJoinList