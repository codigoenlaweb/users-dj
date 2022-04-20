# python

# django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# myapp
from .managers import UserManagers

# Create your models here.


class User(AbstractUser):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'Non binary'),
    )

    # Columns
    first_name = models.CharField(
        verbose_name='First name', max_length=50, blank=False, null=False)
    last_name = models.CharField(
        verbose_name='Last name', max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    email = models.EmailField(
        verbose_name='Email address', max_length=80, unique=True)

    # SuperUser field
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    # Manager class
    objects = UserManagers()

    # Validations
    def clean(self):
        if len(self.first_name) < 2:
            raise ValidationError(
                'The first name must be greater than 2 characters')

        if len(self.last_name) < 2:
            raise ValidationError(
                'The last name must be greater than 2 characters')

    def full_name(self):
        return self.name + ' ' + self.last_name

    def __str__(self):
        return self.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
