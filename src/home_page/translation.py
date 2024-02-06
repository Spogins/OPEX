# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.home_page.models import HomePage


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = ("subtitle",)
