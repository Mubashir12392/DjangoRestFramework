from rest_framework import serializers
from .models import MyItem


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyItem
        fields = "__all__"
