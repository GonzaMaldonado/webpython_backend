import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=50)
  photo = models.ImageField(upload_to='users/', blank=True, null=True)

  REQUIRED_FIELDS = ['email']
  USERNAME_FIELD = 'username'

  def __str__(self):
    if self.first_name == '' and self.last_name == '':
      return f'{self.username}'
    return f'{self.first_name} {self.last_name}'