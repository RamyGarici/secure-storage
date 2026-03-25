from rest_framework import serializers
from .models import File
import os
from .crypto import encrypt
from .crypto_utils import encrypt_key_with_rsa
from django.core.files.base import ContentFile




class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file", "filename"]
    
    


    def create(self, validated_data):
        request = self.context.get("request")


        uploaded_file = validated_data["file"]
        document = uploaded_file.read()

        key = os.urandom(32)
        encrypted_file,iv,tag = encrypt(document,key)
        encrypted_key = encrypt_key_with_rsa(key)

        encrypted_content = ContentFile(
            encrypted_file,
            name = f"{uploaded_file.name}.enc"
        )
   
   
        file = File.objects.create(
            owner = request.user,
            file = encrypted_content,
            filename = validated_data.get("filename", uploaded_file.name),
            encrypted_key = encrypted_key,
            iv=iv,
            tag=tag
            
        )
        return file
    

class FileSerializer(serializers.ModelSerializer):
    class Meta :
        model= File
        fields = ["id", "filename","file","created_at"]