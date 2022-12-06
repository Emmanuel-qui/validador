from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    token = models.UUIDField(primary_key=False, editable=False, null=True)

