from django.db import models 
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

class ValidRollNumber(models.Model):
    roll_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.roll_number

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,roll_number, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        if not roll_number:
            raise ValueError("The Roll Number field must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, roll_number=roll_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, roll_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(username, email, roll_number, password, **extra_fields)



class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=False, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    roll_number = models.CharField(max_length=15)
    depertment = models.CharField(max_length=100, default="CST")

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'roll_number', 'depertment']


    def __str__(self):
        return self.email


