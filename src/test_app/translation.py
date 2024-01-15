# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import TestPage


@register(TestPage)
class TestPageTR(TranslationOptions):
    fields = ("body",)
