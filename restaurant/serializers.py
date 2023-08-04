from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItems, Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id', 'title', 'price', 'inventory']


class UserSerilializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']