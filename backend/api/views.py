from django.db.models.manager import BaseManager
from django.shortcuts import render
from accounts.models import CustomUser
from rest_framework import generics
from accounts.serializers import CustomUserSerializer
from file_transfer.serializers import FileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from file_transfer.models import File


class FileListCreate(generics.ListCreateAPIView):
    """View for adding files and listing existing files"""

    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> BaseManager[File]:
        user = self.request.user
        return File.objects.filter(owner=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)


class FileDelete(generics.DestroyAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> BaseManager[File]:
        user = self.request.user
        return File.objects.filter(owner=user)


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
