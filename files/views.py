from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import FileUploadSerializer


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