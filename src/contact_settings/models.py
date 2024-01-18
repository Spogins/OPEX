# -*- coding: utf-8 -*-
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class ContactSetting(BaseSiteSetting):
    title = models.CharField(max_length=50)
    phone_number_1 = models.CharField(max_length=25)
    phone_number_2 = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    production_address = models.CharField(max_length=255)
    map_coordinates = models.CharField(max_length=100)
    viber = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("phone_number_1"),
        FieldPanel("phone_number_2"),
        FieldPanel("email"),
        FieldPanel("address"),
        FieldPanel("production_address"),
        FieldPanel("map_coordinates"),
        FieldPanel("viber"),
        FieldPanel("telegram"),
        FieldPanel("whatsapp"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("youtube"),
    ]
