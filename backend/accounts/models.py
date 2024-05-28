from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Class representation of users of the web application"""

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    # subscription = models.CharField()
    email = models.EmailField()
    # format for phone number: +233-123-456-789
    phone_number = models.CharField(max_length=13)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """String representation of the class"""
        return self.name
