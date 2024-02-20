# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(verbose_name="Full name", max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(verbose_name="Phone number", max_length=20, blank=True)
    country = models.CharField(verbose_name="Country", max_length=255, blank=True)
    region = models.CharField(verbose_name="Region", max_length=255, blank=True)
    city = models.CharField(verbose_name="City", max_length=255, blank=True)
    address = models.CharField(verbose_name="Address", max_length=255, blank=True)
    user_type = models.CharField(verbose_name="User type", max_length=255, blank=True)
    requisites = models.CharField(verbose_name="Requisites", max_length=255, blank=True)
    legal_country = models.CharField(verbose_name="Legal country", max_length=255, blank=True)
    legal_city = models.CharField(verbose_name="Legal city", max_length=255, blank=True)
    legal_address = models.CharField(verbose_name="Legal address", max_length=255, blank=True)
    postal_code = models.CharField(verbose_name="Postal code", max_length=255, blank=True)
    avatar = models.ImageField(verbose_name="Avatar", upload_to="images", null=True, blank=True)
