from .models import File
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    """ "Serializer class for File"""

    class Meta:
        """The Meta Class"""

        model = File
        fields = [
            "id",
            "owner",
            "file",
            "recepients",
            "public",
            "uploaded_at",
            "last_edited",
        ]
        extra_kwargs = {"public": {"read_only": True}}
