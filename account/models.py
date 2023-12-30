from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, phone, name, password=None):
        if not phone:
            raise ValueError('Users must have an phone number.')
        phone = self.normalize_email(phone)
        user = self.model(phone=phone, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,name,password):
        user = self.create_user(phone, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
class UserProfile(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=20, unique=True, default=None)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name