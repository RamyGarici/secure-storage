from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import FileUploadSerializer, FileSerializer
from .models import File


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
                        status=status.HTTP_204_NO_CONTENT)
    

       
