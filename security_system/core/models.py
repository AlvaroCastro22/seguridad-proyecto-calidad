from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('NORMAL', 'Normal'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # 🔧 FIX: redefinir relaciones para evitar colisión
    groups = models.ManyToManyField(
        Group,
        related_name='core_users',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_users_permissions',
        blank=True
    )

class Application(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

class UserApplicationAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
