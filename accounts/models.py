from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import uuid


class User(AbstractBaseUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin 


class OtpCodeRegister(models.Model):
    phone = models.CharField(max_length=12)
    code = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.phone} - {self.code} - {self.created}'


class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    comment = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user}-{self.title}-{self.status}-{self.created}'