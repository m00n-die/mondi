from django.conf import settings
from django.db import models
from accounts.models import CustomUser


class File(models.Model):
    """Represents the file to be sent"""

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(default=None)
    recepients = models.CharField(max_length=50, default="")
    public = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    # permissions = models.TextChoices()

    def __str__(self) -> str:
        """String representation of the File Class"""
        return self.file.name
