from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.


NEW, CODE_VERIFIED = ("new", "code_verified")


class User(AbstractUser):
    permission_classes = (permissions.AllowAny,)
    REQUIRED_FIELDS = []

    AUTH_STATUS = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
    )

    auth_status = models.CharField(max_length=50, choices=AUTH_STATUS, default=NEW)

    def __str__(self):
        return f'{self.username}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class Branch(models.Model):
    name = models.CharField(max_length=122, verbose_name='Branch Name')

    def __str__(self):
        return f'{self.name}'


class UserBranch(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='branch_user',
    )
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        verbose_name='Branch',
        related_name='branch',
    )
