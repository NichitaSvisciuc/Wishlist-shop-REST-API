from rest_framework import serializers

from .models import *


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = '__all__'


class WhishListSerializer(serializers.ModelSerializer):
	class Meta:
		model = WishList
		fields = '__all__'