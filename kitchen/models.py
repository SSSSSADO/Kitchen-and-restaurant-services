from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "cook"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "dish"

    def get_absolute_url(self):
        return reverse("kitchen:dish-type-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes"
    )

    class Meta:
        verbose_name = "dish type"

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
