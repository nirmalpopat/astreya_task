from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    wins = models.IntegerField(default=0, null=True, blank=True)
    loses = models.IntegerField(default=0, null=True, blank=True)
    ties = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.user)