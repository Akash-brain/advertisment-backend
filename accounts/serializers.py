
from rest_framework import serializers
from .models import User, PartnerApplication, HelpRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "phone", "password"]  # Include all necessary fields
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Ensure password is hashed
        return user

class PartnerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerApplication
        fields = '__all__'

class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        fields = '__all__'

