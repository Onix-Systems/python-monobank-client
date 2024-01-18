from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Mono(models.Model):
    mono_token = models.CharField(
        max_length=44,
        blank=False,
        unique=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.email
