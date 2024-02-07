# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.gallery_page.models import GalleryPage


@register(GalleryPage)
class GalleryPageTranslation(TranslationOptions):
    fields = ("subtitle",)
