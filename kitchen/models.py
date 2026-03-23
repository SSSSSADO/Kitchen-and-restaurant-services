from django.contrib.auth.models import AbstractUser
from django.db import models

class Cook (AbstractUser):
    years_of_experience = models.IntegerField()


class DishType (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
