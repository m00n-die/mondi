from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser Model"""

    class Meta:
        """Meta class for CustomUserSerializer"""

        model = CustomUser
        fields = [
            "id",
            "name",
            "username",
            "email",
            "phone_number",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data) -> CustomUser:
        """Method to create a new CutomUser object"""
        print(validated_data)
        user = CustomUser.objects.create(**validated_data)
        return user
