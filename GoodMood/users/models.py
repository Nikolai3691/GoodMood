from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class ProfileClient(models.Model):
    user = models.ForeignKey('users.CustomUser', blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField('phone number', max_length=24, blank=False, null=False)


class CustomUser(AbstractUser):
    pass

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


