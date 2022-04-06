from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import LANGUAGE_CODE

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = 'male'
    GENDER_OTHER = 'other'
    GENDER_FEMALE = 'female'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_OTHER, 'Other'),
        (GENDER_FEMALE, 'Female'),
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'
    LANGUAGE_CHOISCES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean'),
    )

    CURRUNCY_USD = 'usd'
    CURRUNCY_KRW = 'krw'
    CURRUNCY_CHOICES = (
        (CURRUNCY_USD, 'USD'),
        (CURRUNCY_KRW, 'KRW'),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, null=True, blank=True)
    bio = models.TextField(default='', blank=True)
    birthdate = models.DateField(null=True)
    language = models.TextField(
        choices=LANGUAGE_CHOISCES, max_length=10, null=True, blank=True)
    currency = models.TextField(
        choices=CURRUNCY_CHOICES, max_length=10, null=True, blank=True)
    superhost = models.BooleanField(default=False)
