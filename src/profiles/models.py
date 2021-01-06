from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    """ Custom user model
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    first_login = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')