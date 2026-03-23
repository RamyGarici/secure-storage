from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import FileUploadSerializer, FileSerializer
from .models import File
from .crypto import decrypt
from io import BytesIO


class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, ):
        serializer = FileUploadSerializer(data = request.data,context ={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"File uploaded successfully"},
                status= status.HTTP_201_CREATED
                
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class FileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        files = File.objects.filter(owner = request.user)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
    
    def delete(self, request, id):
        try:
            file = File.objects.get(id=id, owner= request.user)
        except File.DoesNotExist:
            return Response({"message":"File not found"},
                            status= status.HTTP_404_NOT_FOUND)
        file.delete()
        return Response({"message":"File deleted successfully"},
                        status=status.HTTP_200_OK)
    

class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            file_obj = File.objects.get(id=id, owner= request.user)
            file_obj.file.open("rb")
            encrypted_data = file_obj.file.read()
            file_obj.file.close()

        except File.DoesNotExist:
            return Response({"message":"File not found"},
                            status= status.HTTP_404_NOT_FOUND)
        
        file_key =file_obj.key
        file_tag = file_obj.tag
        file_iv = file_obj.iv
        decrypted_file= decrypt(encrypted_data, file_key, file_iv, file_tag)
        return FileResponse(BytesIO(decrypted_file), as_attachment=True, filename=file_obj.filename)
        

        
