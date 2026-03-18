from rest_framework import serializers
from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file", "filename"]
    def create(self, validated_data):
        request = self.context.get("request")
        
        file = File.objects.create(
            owner = request.user,
            file = validated_data["file"],
            filename = validated_data.get("filename", validated_data["file"].name)
        )
        return file