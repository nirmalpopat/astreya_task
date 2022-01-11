from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0, null=True, blank=True)
    loses = models.IntegerField(default=0, null=True, blank=True)
    ties = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.user)