from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'Non binary'),
    )
    
    name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    email = models.EmailField('Email address', unique=True)
    username = models.CharField("Username", max_length=50, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)    
    user_create_date = models.DateTimeField('user created date')
    
    USERNAME_FIELD = 'username'
    
    def full_name(self):
        return self.name + ' ' + self.last_name
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'